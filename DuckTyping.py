class Students:
    def studentnames(self):
        print("kaaliya")
        print("jojo")
        print("Astinos")
        print("Ricardo")

class thirdyear:

    def section(self,other):
        other.studentnames()

stu = Students()
third = thirdyear()

third.section(stu)