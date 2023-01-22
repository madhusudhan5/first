// This is similar to the dictionary in python 

employee = [
    'name' : 'Madhu',
    'Age' : 30
]

println employee
println employee['name']

println employee.get('Age')
println employee.getAt('Age')

println employee.size()

employee.put('city', 'Kolkata')
println employee

employee.each { key, value ->
    println "$key : $value" }

employee.eachWithIndex { key, value, i ->
    println "$i $key : $value" 
}

employee.each { entry ->
    println "$entry.key : $entry.value"
}
