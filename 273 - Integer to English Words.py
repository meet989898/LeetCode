class Solution:
    def numberToWords(self, num: int) -> str:

        # Default edge case
        if num == 0:
            return "Zero"

        # Keep anything above a 999 separate
        big_nums = ["Thousand ", "Million ", "Billion "]

        # Use the helper function to convert anything below 1000
        result = self.small_number_converter(num % 1000)

        # Remove the converted small number
        num = num // 1000

        # Go through the big numbers if any
        for big_num in big_nums:

            # Check to see if the three digits are not zero
            if num > 0 and num % 1000 > 0:

                # Use the same helper function to name the three digits
                result = self.small_number_converter(num%1000) + big_num + result

            # Keep removing three digits at a time
            num = num // 1000

        # Remove any trailing and leading whitespaces
        return result.strip()

    # We use this helper function and pass to it numbers below a 1000. This function helps
    # to convert those numbers to names
    def small_number_converter(self, num: int) -> str:
        units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        result = ""

        while num > 0:

            # Check if there is a digit at the 100 place
            if num > 99:
                result += units[num // 100] + " Hundred "
                num = num % 100

            # Check if the number is not a teen number
            if num > 19:
                result += tens[num // 10] + " "
                num %= 10

            # All the single digits get converted directly
            if 0 < num < 10:
                result += units[num] + " "
                num = num // 10
            else:

                # The remaining case is of the teen numbers, handled directly
                if num > 0:
                    result += teens[num % 10] + " "
                    num = num // 100

        # Return the three digit string that is made
        return result



sol = Solution()
input = 1000000
print(sol.numberToWords(input))