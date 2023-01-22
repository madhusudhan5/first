n=11
if (n%2==0){
    println "Number is even"
}
else{
    println "Number is odd"
}

n=10
switch(n) {
    case 0: println "zero"
            break
    case{n>0}: println "positive"
               break
    case{n<0}: println "negative"
    break
    default: println "Invalid"
    break
}