import java.io.File

fun part1(filePath: String) {
    val file = File(filePath);
    // value is pages that must come after key
    val rules = mutableMapOf<Int, MutableList<Int>>()
    var total = 0

    for (line in file.readLines()) {
        val tmp = line.split("|")
        // build sequence rules
        if (tmp.size == 2) {
            val key = tmp[0].toInt()
            if (rules[key] != null) {
                rules[key]?.add(tmp[1].toInt())
            } else {
                rules[key] = mutableListOf<Int>(tmp[1].toInt())
            }
        } else if (!line.isEmpty()){
            // read page numbers
            val pages = line.split(",");
            var isCorrect = true;
            for (n in 0..pages.size-2) {
                if (rules[pages[n].toInt()]?.contains(pages[n+1].toInt()) != true) {
                    isCorrect = false;
                    break;
                }
            }
            if (isCorrect) {
                total += pages[pages.size/2].toInt()
            }
        }
    }
    println(total)
}

fun part2(filePath: String) {
    val file = File(filePath);
    // value is pages that must come after key
    val rules = mutableMapOf<Int, MutableList<Int>>()
    var total = 0

    for (line in file.readLines()) {
        val tmp = line.split("|")
        // build sequence rules
        if (tmp.size == 2) {
            val key = tmp[0].toInt()
            if (rules[key] != null) {
                rules[key]?.add(tmp[1].toInt())
            } else {
                rules[key] = mutableListOf<Int>(tmp[1].toInt())
            }
        } else if (!line.isEmpty()){
            // read page numbers
            val pages = line.split(",").map{ it -> it.toInt() }.toMutableList();
            var isCorrect = true;
            for (n in 0..<pages.size-1) {
                var m = n;
                // if m+1 is out of place, swap values until order is correct
                while (m >= 0 && rules[pages[m]]?.contains(pages[m+1]) != true) {
                    isCorrect = false;
                    pages[m+1] = pages[m].also { pages[m] = pages[m+1] }
                    m--
                }
            }
            if (isCorrect != true) {
                println(pages)
                total += pages[pages.size/2].toInt()
            }
        }
    }
    println(total)
}

part2("input.txt")