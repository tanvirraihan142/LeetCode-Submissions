class Solution:
    def findLatestTime(self, s: str) -> str:
        time_list = list(s)
    
        # Replace the "?" characters with appropriate digits
        if time_list[0] == "?":
            if time_list[1] == "?" or int(time_list[1]) <= 1:
                time_list[0] = "1"
            else:
                time_list[0] = "0"

        if time_list[1] == "?":
            if time_list[0] == "1":
                time_list[1] = "1"
            else:
                time_list[1] = "9"

        if time_list[3] == "?":
            time_list[3] = "5"

        if time_list[4] == "?":
            time_list[4] = "9"

        # Convert the list back to a string and return
        return "".join(time_list)
