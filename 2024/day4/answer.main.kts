import java.io.File

fun isValid(x: Int, y: Int, sizeX: Int, sizeY: Int) : Boolean {
    return (x in 0 ..sizeX-1) && (y in 0.. sizeY-1)
}

fun findWordInDirection(
    grid: List<String>, word: String, index: Int, x: Int, y: Int, dirX: Int, dirY: Int
): Boolean {
    if (index == word.length) return true

    val rows = grid.count()
    val cols = grid.get(0).length

    if (isValid(x, y, rows, cols) && word.get(index) == grid.get(x).get(y)) {
        return findWordInDirection(
            grid, word, index + 1,
            x + dirX, y + dirY, dirX, dirY
        )
        }
    return false
}

// part 1
fun part1(filePath: String) {
    val file = File(filePath);
    val lines = file.readLines()

    var ans = arrayOf("")
    val rows = lines.count()
    val cols = lines.first().count()

    val word = "XMAS"
    var found = 0;

    // Directions for 8 possible movements
    val directions = arrayListOf(
        Pair(1, 0), Pair(-1, 0), Pair(0, 1), Pair(0, -1),
        Pair(1, 1), Pair (1, -1), Pair(-1, 1), Pair(-1, -1)
    )

    for (i in 0..rows-1) {
        for (j in 0..cols-1) {
            // Check if the first character matches
            if (lines.get(i).get(j) == word.get(0)) {
                for (direction in directions) {
                    if (findWordInDirection(lines, word, 0,
                        i, j, direction.first, direction.second)) {
                        println("($i,$j)")
                        found++;
                        continue
                    }
                }
            }
        }
    }

    println("Found: " + found)

}

part1("input.txt")
