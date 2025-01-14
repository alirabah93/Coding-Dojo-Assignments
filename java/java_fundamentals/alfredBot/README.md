<h1>Alfred Bot</h1>

<p>Objectives:</p>
<ul>
    <li>Be able to implement methods in Java</li>
    <li>Begin using a file with the <code>main</code> method to test your code</li>
    <li>Be able to inject another class instance into your main to use and test methods.</li>
    <li>Import and use the <code>java.util.Date</code> class.</li>
    <li>Practice using <code>String</code> class methods</li>
    <li>Practice using conditional control structures in Java.</li>
</ul>

<hr>

<p>Bruce Wayne's loyal and tireless Butler and best friend, Alfred is getting ready to take some vacation time. He needs to program the Batcomputer to assume his duties through a fully robotic avatar. Although he has mastered numerous arts such as rose breeding, various fields of engineering, nanotechnology, and biotechnology, he doesn't feel like programming his own conversational responses. Therefore, he has contracted you to implement the AlfredQuotes library class. It must rival the "largely unhelpful Alexis", a talking home appliance that Master Wayne bought on Tropics, a large online retailer. To the bat-code!</p>

<h3>java.util</h3>

<p>Throughout this course you will need to import classes from the <code>java.util</code> library. It contains many of the datatypes we will use later in the course like <code>List</code>, <code>ArrayList</code>, <code>HashMap</code>, as well as useful classes like <code>Random</code> and <code>Date</code> to generate pseudo-random numbers.</p>

<h3>AlfredQuotes Class File</h3>

<p>For this Assignment You Will Need 2 Files. First, you'll need an AlfredQuotes.java file that will hold all of the AlfredQuotes functionality. This is where you will do your coding for this assignment. You won't need to compile or run this file directly, as it will be compiled by the AlfredTest.java file. We will also only call/invoke AlfredQuotes methods from within the AlfredTest.java file which is provided.</p>

<p><strong>alfredBot/AlfredQuotes.java</strong></p>

```java
import java.util.Date;
public class AlfredQuotes {
    
    public String basicGreeting() {
        // You do not need to code here, this is an example method
        return "Hello, lovely to see you. How are you?";
    }
    
    public String guestGreeting(String name) {
        // YOUR CODE HERE
        return "place holder for guest greeting return string";
    }
    
    public String dateAnnouncement() {
        // YOUR CODE HERE
        return "place holder for date announcement return string";
    }
    
    public String respondBeforeAlexis(String conversation) {
        // YOUR CODE HERE
        return "for snarky response return string";
    }
    
	// NINJA BONUS
	// See the specs to overload the guestGreeting method
    // SENSEI BONUS
    // Write your own AlfredQuote method using any of the String methods you have learned!
}
```

<h3>Test File</h3>

<p>The methods that belong to the AlfredQuotes file do not execute automatically without the test file. For our Java assignments in this section going forward, you will have two files. But you will only need to compile and run the test file, which will compile the other file as well if there is an instance of that class in the test code. You do not need to alter the following file, although you may if you like.</p>

<p><strong>alfredBot/AlfredTest.java</strong></p>

```java
public class AlfredTest {
    /*
    * This main method will always be the launch point for a Java application
    * For now, we are using the main to test all our 
    * AlfredQuotes methods.
    */
    public static void main(String[] args) {
        // Make an instance of AlfredQuotes to access all its methods.
        AlfredQuotes alfredBot = new AlfredQuotes();
        
        // Make some test greetings, providing any necessary data
        String testGreeting = alfredBot.basicGreeting();
        String testGuestGreeting = alfredBot.guestGreeting("Beth Kane");
        String testDateAnnouncement = alfredBot.dateAnnouncement();
        
        String alexisTest = alfredBot.respondBeforeAlexis(
                            "Alexis! Play some low-fi beats."
                            );
        String alfredTest = alfredBot.respondBeforeAlexis(
            "I can't find my yo-yo. Maybe Alfred will know where it is.");
        String notRelevantTest = alfredBot.respondBeforeAlexis(
            "Maybe that's what Batman is about. Not winning. But failing.."
        );
        
        // Print the greetings to test.
        System.out.println(testGreeting);
        
        // Uncomment these one at a time as you implement each method.
        // System.out.println(testGuestGreeting);
        // System.out.println(testDateAnnouncement);
        // System.out.println(alexisTest);
        // System.out.println(alfredTest);
        // System.out.println(notRelevantTest);
    }
}
```

<h2>Methods to be implemented:</h2>

<h3>Guest Greeting</h3>

<ul>
    <li>Tip: Try using the <code>String.format</code> method for string interpolation in Java.</li>
</ul>

<table>
    <tr>
        <th><strong>Description:</strong></th>
        <th>Returns a greeting that includes the person's name.</th>
    </tr>
    <tr>
        <td><strong>Inputs:</strong></td>
        <td><code>String name</code></td>
    </tr>
    <tr>
        <td><strong>Return Type:</strong></td>
        <td><code>String</code></td>
    </tr>
    <tr>
        <td><strong>Example Output:</strong></td>
        <td>"Hello, Beth Kane. Lovely to see you."</td>
    </tr>
</table>

<h3>Date Announcement</h3>

<table>
    <tr>
        <th><strong>Description:</strong></th>
        <th>Returns a polite announcement of the current date and time.</th>
    </tr>
    <tr>
        <td><strong>Inputs:</strong></td>
        <td>None</td>
    </tr>
    <tr>
        <td><strong>Return Type:</strong></td>
        <td><code>String</code></td>
    </tr>
    <tr>
        <td><strong>Example Output:</strong></td>
        <td>"It is currently Wed Aug 11 16:34:59 PDT 2022."</td>
    </tr>
</table>

<h3>Respond Before Alexis</h3>

<ul>
    <li>Tip: Use the <code>indexOf</code> String method</li>
</ul>

<table>
    <tr>
        <th><strong>Description:</strong></th>
        <th>AlfredBot will periodically process audio (Alfred is listening.) Write a method that accepts any string of conversation and responds appropriately.</th>
    </tr>
    <tr>
        <td><strong>Specifications</strong></td>
        <td>
            <ul>
                <li>If "Alexis" appears in the conversation (in the string) return a snarky response, such as, "Right away, sir. She certainly isn't sophisticated enough for that."</li>
                <li>If "Alfred" is in the conversation return an obliging response, for example, "At your service. As you wish, naturally."</li>
                <li>If neither name is found, return an appropriate response, for instance, "Right. And with that I shall retire."</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><strong>Inputs:</strong></td>
        <td><code>String conversation</code></td>
    </tr>
    <tr>
        <td><strong>Return Type:</strong></td>
        <td><code>String</code></td>
    </tr>
</table>

<h2>Product Back Log (PBL) ~ Ninja Bonuses</h2>

<h3>Guest Greeting (Ninja Bonus Version!)</h3>

<ul>
    <li><strong>Description:</strong> Use method overloading to write another guestGreeting method that returns a greeting including the person's name as well as the day period. Note: It must have the same method name but will have a different method signature.</li>
    <li><strong>Inputs:</strong> String name, String dayPeriod ("morning", "afternoon" or "evening")</li>
    <li>
        <p><strong>Return Type:</strong> String</p>
        <ul>
            <li>Example Output: "Good evening, Beth Kane. Lovely to see you."</li>
        </ul>
    </li>
    <li><strong>SENSEI VERSION:</strong> Instead of a string for the day period, write the overloaded method with no parameters, and use a Date object to determine the day period.</li>
</ul>

<p><strong>Hint:</strong> Use your google-kung-fu! You can use the <code>SimpleDateFormat</code> class and the <code>Format</code> class to help. Both are part of the <code>java.text</code> library. To the <a href="https://docs.oracle.com/javase/8/docs/api/java/text/SimpleDateFormat.html">bat-documentation</a>!</p>


<h4>Sensei Bonus</h4>

<p>Write your own AlfredQuote method using any of the String methods you have learned! For example, maybe he sometimes yells when he's angry.</p>

<h2>A Note About Commenting Your Code</h2>

<p>As you go through this bootcamp, it's a good idea to use comments liberally. Not only will you make your own life easier, but down the line, if you're working on a project and someone else ends up maintaining your code, they will thank you for well-commented code. Likewise, you will appreciate well-commented code in any project you inherit. Many teams and companies will have a style guide for commenting code that you will need to adhere to. In fact, commenting code can also contribute to the autogeneration of documentation in human-readable form. If you're curious about a tool the JDK uses to do this, check out the link for an intro to Javadoc below.</p>

<p><strong>Useful Links</strong></p>
<ul>
    <li><a href="https://docs.oracle.com/javase/8/docs/api/java/util/package-summary.html">java.util</a></li>
    <li><a href="https://docs.oracle.com/javase/8/docs/api/java/util/package-summary.html">Java String documentation</a></li>
    <li><a href="https://www.baeldung.com/javadoc">Javadoc</a></li>
</ul>

<p>To Do List:</p>
<ul>
    <li>Create a project folder in your Java course folder called "alfredBot"</li>
    <li>Create an AlfredQuotes.java class file that will hold all of Alfred bot's functionality.</li>
    <li>Create an AlfredTest.java main program file that will execute code to test our AlfredQuotes class.</li>
    <li>Implement the guestGreeting method, and test it by first compiling the test file with the javac command and then running the test file with the java command in your terminal.</li>
    <li>Implement the dateAnnouncement method, and test it.</li>
    <li>Implement the answeringBeforeAlexis method, and test it.</li>
    <li>NINJA BONUS: Implement your own method for the Alfred bot using any of the built-in String methods you've learned. Maybe he can yell..</li>
</ul>


