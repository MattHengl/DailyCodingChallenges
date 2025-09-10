using System;
using System.Reflection.Metadata.Ecma335;
using System.Text.Json;
using System.Threading.Tasks;
using System.Transactions;

namespace BankingSystem;
class BankingSystem
{
    public static List<Account> accountDatabase = new List<Account>();
    static void Main(string[] args)
    {
        /*
         * Banking System
         * Manage multiple bank account
         * - account $, account holder name, balance
         * - account type(checking, saving, business)
         * - tranaction history
         * Support Core Banking Operations
         * - create new account
         * - deposit/withdraw money
         * - transfer money between accounts
         * - check account balance and transaction history
         * Generate account statements showing
         * - recent transactions with timestamps
         * - monthly summaries
         * - account details and current balance
         * Apply Simple Business Rules
         * - minimun balance requirements for different account types
         * - transaction fees for certain operations
         * - interest calculation for saving accounts(simple interest)
         * SAVING ALL DATA TO FILES FOR PERSISTENCE
         */
        accountDatabase = BankOperations.LoadJson();
        bool accountFound = false;
        Account account = null;
        Console.WriteLine("Hello! \nDo you have an account already?(Y/N)");
        if (Console.ReadLine().ToLower().Contains("y"))
        {
            do
            {
                Console.WriteLine("What is the number of your account?");
                string wantedAccountNumber = Console.ReadLine();
                accountFound = BusinessRules.CheckIfAccountExists(wantedAccountNumber);
                if (accountFound == false)
                {
                    Console.WriteLine("Account was not found. Do you want to try anouther account number?");
                    if (Console.ReadLine().ToLower().Contains("y"))
                    {
                        accountFound = false;
                    }
                    else
                    {
                        break;
                    }
                }
                else
                {
                    account = accountDatabase.FirstOrDefault(acc => acc.AccountNumber == wantedAccountNumber);
                }
            } while (!accountFound);
        }
        if (accountFound == false)
        {
            Console.WriteLine("Lets create your account then!");
            account = BankOperations.CreateAccount();
            accountDatabase.Add(account);
        }
        bool flag = true;
        do
        {
            Console.WriteLine("What do you want to do?");
            string action = Console.ReadLine();
            switch (action.ToLower())
            {
                case "deposit":
                    BankOperations.DepositFunds(account);
                    break;
                case "withdraw":
                    BankOperations.WithdrawFunds(account);
                    break;
                case "transfer":
                    BankOperations.TransferFunds(account);
                    break;
                case "balance":
                    Console.WriteLine(BankOperations.CheckAccountBalance(account)); 
                    break;
                case "history":
                    BankOperations.AccountTransactionHistory(account);
                    break;
                case "exit":
                    flag = false;
                    break;
                default:
                    break;
            }
        } while (flag);
        BankOperations.SaveToJson(accountDatabase);
    }
}

class BankOperations 
{
    public static Account CreateAccount()
    {
        Random rand = new Random();
        Console.WriteLine("What's the first name on the account?");
        string firstName = Console.ReadLine();
        Console.WriteLine("What's the last name on the account?");
        string lastName = Console.ReadLine();
        Console.WriteLine("What type of account do you want to make?(checking, saving, business)");
        string accountType = Console.ReadLine();
        string accountNumber = "A" + rand.Next(0, 100001);
        return new Account(accountNumber, firstName, lastName, 0.00, accountType);
    }
    public static void DepositFunds(Account account)
    {
        Random rand = new Random();
        Console.WriteLine("How much do you want to deposit into your account?");
        double depositAmount = double.TryParse(Console.ReadLine(), out var result) ? result : 0.0;
        account.Balance += depositAmount;
        Transaction newTransaction = new Transaction(DateTime.Now, "D" + rand.Next(0,100001), account.GetAccountNumber(), account.GetAccountNumber(), depositAmount);
        account.AddTransaction(newTransaction);
    }
    public static void WithdrawFunds(Account account)
    {
        Console.WriteLine("How much do you want to withdraw from the account?");
        double withdrawalAmount = double.TryParse(Console.ReadLine(), out var result) ? result : 0.0;
        if (IsZero(account.Balance - withdrawalAmount))
        {
            Random rand = new Random();
            account.Balance = BusinessRules.AddTransactionFees(account.Balance, withdrawalAmount, "withdraw");
            Transaction newTransaction = new Transaction(DateTime.Now, "W" + rand.Next(0, 100001), account.GetAccountNumber(), account.GetAccountNumber(), withdrawalAmount);
            account.AddTransaction(newTransaction);
        }
        else
        {
            Console.WriteLine("You account doesn't have enough funds to withdraw that amount");
            Console.WriteLine("Amount: " + account.Balance);
        }
    }
    public static void TransferFunds(Account account)
    {
        Random rand = new Random();
        Account recievingAccount = null;
        Console.WriteLine("What bank account do you want to transfer funds to?");
        string wantedAccount = Console.ReadLine();
        if (BusinessRules.CheckIfAccountExists(wantedAccount))
        {
            recievingAccount = BankingSystem.accountDatabase.FirstOrDefault(acc => acc.AccountNumber == wantedAccount);
            Console.WriteLine("How much money do you want to transfer?");
            double transferAmount = double.TryParse(Console.ReadLine(), out var result) ? result : 0.0;
            if (IsZero(account.Balance - transferAmount))
            {
                account.Balance -= transferAmount;
                Transaction newTransaction = new Transaction(DateTime.Now, "T" + rand.Next(0, 100001), account.GetAccountNumber(), recievingAccount.AccountNumber, transferAmount);
                account.AddTransaction(newTransaction);
                recievingAccount.Balance -= transferAmount;
                recievingAccount.AddTransaction(newTransaction);
            }
        }
        else
        {
            Console.WriteLine("The account that you want to send money to doesn't exist");
        }
    }
    public static string CheckAccountBalance(Account account)
    {
        return account.GetCurrentBalance();
    }
    public static void AccountTransactionHistory(Account account)
    {
        account.PrintTransactionHistory();
    }
    public static bool IsZero(double balance)
    {
        return balance > 0 ? true : false;
    }
    public static List<Account> LoadJson()
    {
        string jsonString = File.ReadAllText("../../../BankDatabase.json");
        var accounts = JsonSerializer.Deserialize<List<Account>>(jsonString) ?? new List<Account>();
        return accounts;
    }
    public static void SaveToJson(List<Account> accounts)
    {
        string jsonString = JsonSerializer.Serialize(accounts, new JsonSerializerOptions { WriteIndented = true });
        File.WriteAllText("../../../BankDatabase.json", jsonString);
    }
}

class BusinessRules
{
    public static bool CheckIfAccountExists(string accountNumber)
    {
        bool found = false;
        foreach (Account acc in BankingSystem.accountDatabase)
        {
            if (acc.AccountNumber == accountNumber)
            {
                found = true;
            }
        }
        return found ? true : false;
    }
    public static bool CheckForMinBalance(double balance)
    {
        return balance > 2.50? true: false;
    }
    public static double AddTransactionFees(double balance, double transactionAmount, string transaction)
    {
        switch (transaction.ToLower())
        {
            case "deposit":
                return ((balance + transactionAmount) - 3.50) > 0 ? (balance + transactionAmount) - 3.50 : 0.00;
            case "withdraw":
                return ((balance - transactionAmount) - 3.50) > 0 ? (balance - transactionAmount) - 3.50 : 0.00;
            default:
                return 0.00;
        }
    }
    public static double InterestCalculation(int interestAmount)
    {
        return interestAmount * .5 * 5;
    }
}
public class Account
{
    public string AccountNumber { get; set; }
    public string GetAccountNumber()
    {
        return AccountNumber;
    }
    public string FirstName {  get; set; }
    public string LastName { get; set; }
    public double Balance {  get; set; }
    public string AccountType { get; set; }
    public List<Transaction> TransactionHistory { get; set;}

    public Account()
    {
        TransactionHistory = new List<Transaction>();
    }
    public Account(string accountNumber, string firstName, string lastName, double balance, string accountType)
    {
        AccountNumber = accountNumber;
        FirstName = firstName;
        LastName = lastName;
        Balance = balance;
        AccountType = accountType;
        TransactionHistory = new List<Transaction>();
    }
    public void AddTransaction(Transaction transaction)
    {
        TransactionHistory.Add(transaction);
    }

    public string ToString()
    {
        return "Account Number: " + AccountNumber + "\nName on Account: " + FirstName + LastName + "\nBalance: $" + Balance + "Account Type: " + AccountType;
    }
    public string GetCurrentBalance()
    {
        return "Current Balance: $" + Balance;
    }
    public void PrintTransactionHistory()
    {
        foreach (Transaction transaction in TransactionHistory)
        {
            Console.WriteLine(transaction.ToString());
            Console.WriteLine();
        }
    }
    public string ShowTransactionHistory() { return "no"; }
}
public class Transaction
{
    public DateTime TransactionDate { get; set; }
    public string TransactionNumber { get; set; }
    public string SendingAccountNumber { get; set; }
    public string RecievingAccountNumber { get; set; }
    public double AmountSent { get; set; }
    public Transaction(DateTime transactionDate, string transactionNumber, string sendingAccountNumber, string recievingAccountNumber, double amountSent)
    {
        TransactionDate = transactionDate;
        TransactionNumber = transactionNumber;
        SendingAccountNumber = sendingAccountNumber;
        RecievingAccountNumber = recievingAccountNumber;
        AmountSent = amountSent;
    }
    public string ToString()
    {
        return "TransactionDate: " + TransactionDate.ToString() + "\nTransactionNumber: " + TransactionNumber + "\nSending Account Number: " + SendingAccountNumber + "\nRecievingAccountNumber: " + RecievingAccountNumber + "\nAmountSent: " + AmountSent;
    }
}
