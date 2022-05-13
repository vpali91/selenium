using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SeleniumTutorial3
{
    class Program
    {
        static void Main(string[] args)
        {
            var driver = new ChromeDriver();
            ITakesScreenshot screenshotDriver = driver as ITakesScreenshot;

            driver.Url = "https://google.com";
            driver.Manage().Window.Maximize();
            Screenshot screenshot = screenshotDriver.GetScreenshot();
            screenshot.SaveAsFile("d:/test1.png");

            driver.Navigate().GoToUrl(@"https://facebook.com");
            Screenshot screenshot2 = screenshotDriver.GetScreenshot();
            screenshot2.SaveAsFile("d:/test2.png");
            driver.Navigate().GoToUrl(@"https://bing.com");
            Screenshot screenshot3 = screenshotDriver.GetScreenshot();
            screenshot3.SaveAsFile("d:/test3.png");
            IWebElement element = driver.FindElement(By.Id("sb_form_q"));
            element.SendKeys("someText" + Keys.Enter);
            Screenshot screenshot4 = screenshotDriver.GetScreenshot();
            screenshot4.SaveAsFile("d:/test4.png");

            driver.Navigate().GoToUrl(@"https://www.tests.com/login");
            IWebElement element2 = driver.FindElement(By.Name("em"));
            element2.SendKeys("asd");
            IWebElement element3 = driver.FindElement(By.Name("pw"));
            element3.SendKeys("dsadaf");

            IWebElement element4 = driver.FindElement(By.Name("Login"));
            element4.Click();
        }
    }
}
