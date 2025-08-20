//Matt Hengl
//8/19/2025

namespace FileOrganizer;

class FileOrganizer
{
    static void Main(string[] args)
    {
        //Check to see if the file path from the params exists at all in the PC
        // If it does, continue
        // If it does not, then tell the user that that file path does not exist
        //Once the path is confirmed, go to that file path and start to read in the files in the folder
        //For each file, check the file extension
        //For each file extension, create a folder if it does not exist
        //If it does, then skip this step
        //Once the new folder is created, then move all the files with that extension to that folder(Documents, Images, Videos, etc.)
        //Move onto the next file
        //Keep a running count of which file types got moved
        //Make sure to add some error handling
        //Think about dupblicated files and files that cant be moved

        OrganizerPayload organizerObject = new OrganizerPayload();
        try
        {
            Console.WriteLine("Starting Application");
            organizerObject.Path = Console.ReadLine();
            Console.WriteLine(organizerObject.Path);

            CheckPathExists(organizerObject);
            if (organizerObject.Success == true)
            {
                Console.WriteLine("Pathing Exists");
                Directory.SetCurrentDirectory(organizerObject.Path);
                CreateFolderIfNotExists(organizerObject);
                string[] fileArray = Directory.GetFiles(organizerObject.Path);
                foreach (var file in fileArray)
                {
                    MoveFileIntoNewFolder(organizerObject, file);
                }
            }
            else
            {
                throw new Exception(organizerObject.Message);
            }

            if (organizerObject.Success == false)
            {
                throw new Exception();
            }
        }
        catch (Exception e)
        {
            Console.WriteLine(organizerObject.Message);
        }
    }
    private static void CheckPathExists(OrganizerPayload organizerObject)
    {
        Console.WriteLine("CheckPathExists");
        if (!Directory.Exists(organizerObject.Path))
        {
            organizerObject.Success = false;
            organizerObject.Message = "File path does not exist";
            Console.WriteLine("File path does not exist");
        }
    }
    private static void CreateFolderIfNotExists(OrganizerPayload organizerObject)
    {
        try
        {
            Console.WriteLine("CreateFolderIfNotExists");
            Directory.CreateDirectory("Pictures");
            Directory.CreateDirectory("Documents");
            Directory.CreateDirectory("Downloads");
            Directory.CreateDirectory("Videos");
            Directory.CreateDirectory("Music");
            Directory.CreateDirectory("Other");
        }
        catch (Exception e)
        {
            organizerObject.Success = false;
            organizerObject.Message = "Folders could not be created";
        }
    }
    private static void MoveFileIntoNewFolder(OrganizerPayload organizerObject, string file)
    {
        try
        {
            Console.WriteLine("MoveFileIntoNewFolder");
            Console.WriteLine(file);
            Console.WriteLine(Path.GetExtension(file));
            switch (Path.GetExtension(file))
            {
                case ".txt":
                case ".pdf":
                    Console.WriteLine(Path.Combine(organizerObject.Path, "Documents", Path.GetFileName(file)));
                    File.Move(file, Path.Combine(organizerObject.Path, "Documents", Path.GetFileName(file)), true);
                    break;
                case ".png":
                case ".jpg":
                    Console.WriteLine(Path.Combine(organizerObject.Path, "Pictures", Path.GetFileName(file)));
                    File.Move(file, Path.Combine(organizerObject.Path, "Pictures", Path.GetFileName(file)), true);
                    break;
                case ".exe":
                    Console.WriteLine(Path.Combine(organizerObject.Path, "Other", Path.GetFileName(file)));
                    File.Move(file, Path.Combine(organizerObject.Path, "Other", Path.GetFileName(file)), true);
                    break;
                case ".zip":
                    Console.WriteLine(Path.Combine(organizerObject.Path, "Downloads", Path.GetFileName(file)));
                    File.Move(file, Path.Combine(organizerObject.Path, "Downloads", Path.GetFileName(file)), true);
                    break;
                default:
                    break;
            }
        }
        catch (Exception e)
        {
            organizerObject.Success = false;
            organizerObject.Message = e.Message;
        }
    }

    class OrganizerPayload
    {
        public bool Success { get; set; }
        public string Message { get; set; }
        public string Path { get; set; }
        public OrganizerPayload(bool success, string message, string path)
        {
            Success = success;
            Message = message;
            Path = path;
        }
        public OrganizerPayload()
        {
            Success = true;
            Message = "";
            Path = "";
        }
    }
}