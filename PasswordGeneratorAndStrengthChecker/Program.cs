namespace PasswordGeneratorAndChecker;

class PassGenAndChecker
{
    static void Main(string[] args)
    {
        //Set up a menu where the user can select either generate password OR checking the strength on a password
            //If password
                //Generate a random password without (0/o/1/i/I)
                //Save it to a file
            //If check mode
                //Get a password from either the user or read in each password from the file and display the strength of the password
                    //Get input from the user
                        //Just give the strength of the password
                    //Read in from the file
                        //Display the password and then display the strength of the password in a list format
        //Have a black list of passwords that if the password being input contains something on that list, it will either:
            //Generate a new password OR tell the user that they will have to generate a new password
        Console.WriteLine("Do you want to generate a password or check the strength of a password? ");
        string option = Console.ReadLine().ToLower();
        if (option.Contains("generate"))
        {
            Console.WriteLine("Do you want to input your own password or generate a random one?");
            string password = "";
            if (Console.ReadLine().ToLower().Contains("generate"))
            {
                Console.WriteLine("Going to generate 10 random passwords for you.");
                for(int i = 0; i <= 10; i++)
                {
                    Random rand = new Random();
                    int length = rand.Next(4, 20);
                    for(int j = 0; j <= length; j++)
                    {
                        int stringOrInt = rand.Next(0,2);
                        //0 = int
                        //1 = string
                        if(stringOrInt == 0)
                        {
                            int randomInt = rand.Next(0,11);
                            password += randomInt.ToString();
                        }
                        else
                        {
                            int randomString = rand.Next(0, 26);
                            char letter = Convert.ToChar(randomString + 65);
                            password += letter;
                        }
                    }
                    WritePassword(password);
                    Console.WriteLine(password);
                    password = "";
                }
            }
            else
            {
                Console.WriteLine("What password do you want to enter?");
                password = Console.ReadLine();
                List<string> blackList = loadFile("../../../passwordBlacklist.txt");
                if (blackList.Contains(password))
                {
                    Console.WriteLine("Your password is a commonly used password. Sorry, pick another one.");
                }
                else
                {
                    Console.WriteLine("Password is good! Saved!");
                    WritePassword(password);
                }
            }
        }
        else if (option.Contains("check"))
        {
            Console.WriteLine("Do you want to input your own password or read in from the password file?");
            if (Console.ReadLine().Contains("input"))
            {
                Console.WriteLine("What passowrd do you want to check?");
                string password = Console.ReadLine();
                Console.WriteLine(password + " strength is " + passwordChecker(password));
            }
            else
            {
                List<string> listOfPasswords = loadFile("../../../savedPasswords.txt");
                foreach (string password in listOfPasswords)
                {
                    Console.WriteLine(password + " strength is " + passwordChecker(password));
                }
            }
        }
    }
    public static void WritePassword(string password)
    {
        using (StreamWriter writer = new StreamWriter("../../../savedPasswords.txt", append: true))
        {
            writer.WriteLine(password);
        }
    }
    public static List<string> loadFile(string path) 
    {   
        List<string> passwordBlackList = new List<string>();
        using (StreamReader reader = new StreamReader(path))
        {
            while (reader.Peek() != -1)
            {
                passwordBlackList.Add(reader.ReadLine());
            }
        }
        return passwordBlackList;
    }
    public static string passwordChecker(string password)
    {
        //Takes in the password
        //Checks to see if the password has atleast 1 special character
        //Checks to see if the password has atlease 2 numbers
        //Checks to see if the password is 8+ characters in length
        //Checks to see if the password has any characters that are the same that as next to each other
        //Checks to see if the password is not in the blacklist file
        //If any of these are true, then add 1 to the score
        //1 = Weak
        //2 = Fair
        //3 = Good
        //4 = Strong
        //5 = Excellent
        int score = 0;
        if (ContainsSpecialCharacters(password))
        {
            //Console.WriteLine("ContainsSpecialCharacters = true");
            score++;
        }
        if (ContainsMoreThanTwoNumbers(password))
        {
            //Console.WriteLine("ContainsMoreThanTwoNumbers = true");
            score++;
        }
        if (IsLengthGreaterThanEight(password))
        {
            //Console.WriteLine("IsLengthGreaterThanEight = true");
            score++;
        }
        if (CheckingIfCharactersAreTheSame(password))
        {
            //Console.WriteLine("CheckingIfCharactersAreTheSame = true");
            score++;
        }
        List<string> blacklist = loadFile("../../../passwordBlacklist.txt");
        if (!blacklist.Contains(password))
        {
            //Console.WriteLine("InBlackList = true");
            score++;
        }
        switch (score)
        {
            case 2:
                return "Fair";
            case 3:
                return "Good";
            case 4:
                return "Strong";
            case 5:
                return "Excellent";
            default:
                return "Weak";
        }
    }
    public static bool ContainsSpecialCharacters(string password)
    {
        return password.Any(c => !Char.IsLetterOrDigit(c));
    }
    public static bool ContainsMoreThanTwoNumbers(string password)
    {
        int numOfNums = 0;
        char[] passwordInChars = password.ToCharArray();
        for(int i = 0; i < passwordInChars.Length ; i++)
        {
            if (Char.IsDigit(passwordInChars[i]))
            {
                numOfNums++;
            }
        }
        if(numOfNums > 2 )
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    public static bool IsLengthGreaterThanEight(string password) 
    {
        if(password.Length > 8)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    public static bool CheckingIfCharactersAreTheSame(string password)
    {
        char[] passwordInChars = password.ToCharArray();
        for(int i = 0; i < passwordInChars.Length - 1; i++)
        {
            if (passwordInChars[i] == passwordInChars[i + 1])
            {
                return false;
            }
        }
        return true;
    }
} 
