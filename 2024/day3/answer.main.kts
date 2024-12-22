import java.io.File

val filePath = "input.txt";
val file = File(filePath);

// part 1
fun part1(file: File) {
    val regex = """mul\([0-9]+,[0-9]+\)""".toRegex()
    val regex2 = """[0-9]+""".toRegex()
    var sum = 0;

    for (line in file.readLines()) {
        var results = regex.findAll(line);
        for (result in results) {
            var nums = regex2.findAll(result.value);
            sum += nums.first().value.toInt() * nums.last().value.toInt();
            println(result.value + " " + nums.first().value + " " + nums.last().value)
        }
    }
    print("Total: " + sum)
}

fun part2(file: File) {
    var sum = 0;
    var text = file.readText()
    val regex = """(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))""".toRegex()
    val regex2 = """[0-9]+""".toRegex()

    var results = regex.findAll(text)
    var isValid = true;
    for (result in results) {
        if (result.value == "do()") isValid = true;
        if (result.value == "don't()") isValid = false;
        if (isValid && result.value.startsWith("mul")) {
            var nums = regex2.findAll(result.value);
            sum += nums.first().value.toInt() * nums.last().value.toInt();
            println(result.value + " " + nums.first().value + " " + nums.last().value)
        }
    }
    print("Total: " + sum)

}

if (file.exists()) {
//    part1(file)
    part2(file)
} else {
    println("File not found.")
}