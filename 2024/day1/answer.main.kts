#!/usr/bin/env kotlin

import java.io.File
import kotlin.math.abs

// part 1
val filePath = "input.txt"
val file = File(filePath)

if (file.exists()) {
    val left = mutableListOf<Int>()
    val right = mutableListOf<Int>()

    // load content into arrays
    for (line in file.readLines()) {
        val values = line.split("   ")
        left.add(values.get(0).toInt())
        right.add(values.get(1).toInt())
    }

    // sort arrays
    left.sort()
    right.sort()

    // compute distance
    var total = 0
    for (n in 0..left.lastIndex) {
        total += abs(left.get(n) - right.get(n))
    }

    println("Part 1 answer: $total")

} else {
    println("File not found.")
}

