# sort the character in string by their frequency
msg_given = 'csestack'
msg_alpha = sorted(msg_given)
sorted_list = sorted(msg_alpha, key=lambda c: msg_alpha.count(c))
final_msg = "".join(sorted_list)
print(final_msg)