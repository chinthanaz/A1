<!DOCTYPE html>
<html>
<head>
    <title>Multiplication</title>
</head>
<body>
    <h1>Multiplication of Two Numbers</h1>
    <form method="post" action="">
        <label for="num1">Enter the first number:</label>
        <input type="text" name="num1" id="num1" required><br><br>
        
        <label for="num2">Enter the second number:</label>
        <input type="text" name="num2" id="num2" required><br><br>
        
        <input type="submit" name="submit" value="Multiply">
    </form>

    <?php
    if(isset($_POST['submit'])){
        // Get the values entered by the user
        $num1 = $_POST['num1'];
        $num2 = $_POST['num2'];

        // Perform the multiplication
        $result = $num1 * $num2;

        // Display the result
        echo "<p>The result of multiplying $num1 and $num2 is: $result</p>";
    }
    ?>
</body>
</html>
