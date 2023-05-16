# FizzBuzz

stop = 100
for i in range(1, stop + 1):
    fb_nums = [3, 5, 7, 8, 12, 4]
    fb_outs = ['Fizz', 'Buzz', 'Whizz', 'Bang', 'Snap', 'Naqibo']
    output = ''
    for j in range(len(fb_nums)):
        if not(i % fb_nums[j]):
            output += fb_outs[j]
    if len(output) == 0:
        output += str(i)
    # print(output)
