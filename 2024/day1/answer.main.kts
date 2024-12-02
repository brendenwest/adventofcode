#!/usr/bin/env kotlin

import java.io.File
import kotlin.math.abs

// part 1
val filePath = "input.txt"
val file = File(filePath)

fun part1(file: File) {
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

}

fun part2(file: File) {
    val left = mutableListOf<Int>()
    val right = mutableMapOf<Int, Int>()

    // load content into array & map
    for (line in file.readLines()) {
        val values = line.split("   ")
        left.add(values.get(0).toInt())
        val key = values.get(1).toInt()
        right[key] = right.getOrDefault(key, 0) + 1
    }

    var total = 0
    for (n in 0..left.lastIndex) {
        val num = left.get(n)
        val count = right.getOrDefault(num, 0)
        total += num * count
    }

    println("Part 2 answer: $total")

}

if (file.exists()) {
    part1(file)
    part2(file)

} else {
    println("File not found.")
}

