<!DOCTYPE html>
<html>
<head>
    <title>Calculate Sum</title>
</head>
<body>
    <h2>Enter Two Numbers to Calculate Sum</h2>
    <form method="POST">
        <label for="num1">Number 1:</label>
        <input type="number" name="num1" id="num1" required>
        <br><br>
        <label for="num2">Number 2:</label>
        <input type="number" name="num2" id="num2" required>
        <br><br>
        <input type="submit" name="submit" value="Calculate Sum">
    </form>

    <?php
    // Check if the form is submitted
    if (isset($_POST['submit'])) {
        // Retrieve the values of num1 and num2 from the form
        $num1 = $_POST['num1'];
        $num2 = $_POST['num2'];

        // Calculate the sum
        $sum = $num1 + $num2;

        // Display the sum
        echo "<h3>The sum of $num1 and $num2 is: $sum</h3>";
    }
    ?>
</body>
</html>

