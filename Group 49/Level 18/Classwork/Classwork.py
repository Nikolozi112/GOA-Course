# 1) შექმენით 3 list'ი და სამივეც მიეცით 5 სხვადასხვა მნიშვნელობა, ასევე კომენტარის სახით ყველას მიუწერეთ ინდექსები
# 2) Indexing'ის მეშვეობით ყველა ლისტიდან გამოიტანეთ მეხუთე ანუ ბოლო ელემენტი

nums = [5, 82, 524, 23, 4562]
#       0   1   2    3    4
word = ["Bus", "House", "TV", "Door", "Book"]
#          0       1      2     3        4
planets = ["Mars", "Venus", "Jupiter", "Earth", "Saturn"]
#             0       1         2         3        4

print(nums[4])
print(word[4])
print(planets[4])

# 3) ndexing'ის მეშვეობით გამოიტანეთ სიტყვა "sunglasses"

words = ["rise", "sun", "glasses"]

print(words[1] + words[2])

# 4) შექმენით კიდევ ერთი list'ი და Indexing'ის მეშვეობით შეუცვალეთ ბოლო ელემენტის მნიშვნელობა

list = ["Earth", 7, "Snowman", 42]
list.insert(4, 12) 
print(list)

# 5) ახსენით რას ნიშნავს mutable

# mutable ნიშნავს, რომ ობიექტის შინაარსი შეიძლება შეიცვალოს პროგრამის მუშაობის პროცესში.