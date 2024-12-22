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

if (file.exists()) {
    part1(file)
} else {
    println("File not found.")
}