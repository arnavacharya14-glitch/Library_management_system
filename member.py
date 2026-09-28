class MemberManager:
    def __init__(self):
        self.members = []
        self.next_member_id = 1

    def register_member(self):
        name = input("Enter your name: ")
        email = input("Enter E-mail ID: ")

        try:
            phone = int(input("Enter phone no.: "))
        except ValueError:
            print("Invalid phone number.")
            return

        member = {
            "id": self.next_member_id,
            "name": name,
            "email": email,
            "phone": phone
        }

        self.members.append(member)
        print("Assigned member ID:", self.next_member_id)
        self.next_member_id += 1

    def get_member(self, member_id):
        for member in self.members:
            if member["id"] == member_id:
                return member
        return None

    def find_member_by_name(self, name):
        for member in self.members:
            if member["name"].lower() == name.lower():
                return member
        return None
