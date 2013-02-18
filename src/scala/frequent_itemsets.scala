// def apriori(transactions: List[Set[Int]]):Set[Int] = {
//     // Generate candidate 1-itemsets
// 
//     val = transactions
// 
// }

def counter[A](sequence: List[A], counts: Map[A, Int]):Map[A, Int] = {
    // base case
    if(sequence.isEmpty) {
        return counts
    }

    // recursive
    val new_count = (counts getOrElse (sequence.head, 0))	+ 1
    val updated_counts = counts + (sequence.head -> new_count)
    return counter(sequence.tail, updated_counts)
}

def counter[A](sequence: List[A]): Map[A, Int] = {
    sequence.foldLeft(Map() : scala.collection.immutable.Map[A, Int]) ( (acc, item ) => acc + (item -> ((acc getOrElse (item, 0)) + 1)))
}

// don't forget to fill in blank map
var myList = List(1,23,34,1)
println(myList)
println(counter(myList, Map()))
println()

var myList2 = List("hi", "world", "hi")
println(myList2)
println(counter(myList2, Map()))
println()

// folding

