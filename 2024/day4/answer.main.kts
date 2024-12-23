import java.io.File
import java.util.ArrayList

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

fun findWord(
    grid: List<String>, word: String, index: Int, x: Int, y: Int, dirX: Int, dirY: Int,
    pairs: ArrayList<Pair<Int,Int>> = arrayListOf()
): ArrayList<Pair<Int,Int>>? {
    if (index == word.length) return pairs

    val rows = grid.count()
    val cols = grid.get(0).length
    pairs.add(Pair(x,y))

    if (isValid(x, y, rows, cols) && word.get(index) == grid.get(x).get(y)) {
        return findWord(
            grid, word, index + 1,
            x + dirX, y + dirY, dirX, dirY, pairs
        )
    }
    return null
}

// part 1
fun part1(filePath: String, word: String) {
    val file = File(filePath);
    val lines = file.readLines()

    val rows = lines.count()
    val cols = lines.first().count()

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

// part 2
fun part2(filePath: String, word: String) {
    val file = File(filePath);
    val lines = file.readLines()
    val rows = lines.count()
    val cols = lines.first().count()
    var centerPoints: ArrayList<Pair<Int,Int>> = arrayListOf()

    var found = 0;

    // Directions for 8 possible movements
    val directions = arrayListOf(
        Pair(1, 1), Pair (1, -1), Pair(-1, 1), Pair(-1, -1)
    )

    for (i in 0..rows-1) {
        for (j in 0..cols-1) {
            // Check if the first character matches
            if (lines.get(i).get(j) == word.get(0)) {
                for (direction in directions) {
                    var pairs = findWord(lines, word, 0,
                    i, j, direction.first, direction.second)
                    if (pairs != null) {
                        println("($i,$j) $pairs")
                        if (pairs.get(1) in centerPoints) { found++ }
                        else { centerPoints.add(pairs.get(1)) }
                        continue
                    }
                }
            }
        }
    }
    println("Found: " + found)

}

part2("input.txt", "MAS")
