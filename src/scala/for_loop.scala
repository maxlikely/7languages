def forLoop {
    println("for loop using java iteration")
    for(i <- 0 until args.length) {
        println(args(i))
    }
}
forLoop
// vim: set ts=4 sw=4 et:
