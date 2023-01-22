// Strings                                 Multiline            Interpolation(Variable)
// -------------------------------------------------------------------------------------
// Single Qoutes     '...............'         Y                       N
// Double Qoutes     ".............."          Y                       Y
// Triple Single Qoutes '''......'''           Y                       N
// Triple Double Qoutes """....."""            Y                       Y
// Slashy              /.........../           Y                       Y
// Dollar Slashy       $/........../$          Y                       Y

name = "Madhu"
println name

println "My name is $name"
println 'My name is $name'

s1 = '''This is groovy
learning session'''

println s1

println name.length()
println name
println name[2]

println name[-1]

println name[2..4]
println name[4..2]

println name.indexOf('d')

println name.substring(2)


str = "I live at Adra"

println str
println str.split(' ')
println str-("at")
println str.replace("Adra","Kolkata")

println str.toLowerCase()
println str.toUpperCase()

println str.toList()

println "Madhu " * 3

println "Abc".equals("Abc")
println "Abc".equals("abc")
println "Abc".equalsIgnoreCase("abc")



s1 = /a green
    sky $name/
s2 = $/a blue 
    tree $name/$
println s1
println s2

s3 = "My name is \"Madhu\""
s4 = /My name is "Madhu"/
println s3
println s4