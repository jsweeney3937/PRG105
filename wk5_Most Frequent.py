

def main():
    # sets user_input to value returned from function get_user_input
    user_input = get_user_input()
    # runs function count_most_frequent_letters with user_input passed as argument
    count_most_frequent_letters(user_input)


def get_user_input():
    # gets a string from the user
    user_string = input("Enter a phrase. ")
    # returns strings value
    return user_string


def count_most_frequent_letters(user_input):
    # sets count "letter" to 0
    c_a = 0
    c_b = 0
    c_c = 0
    c_d = 0
    c_e = 0
    c_f = 0
    c_g = 0
    c_h = 0
    c_i = 0
    c_j = 0
    c_k = 0
    c_l = 0
    c_m = 0
    c_n = 0
    c_o = 0
    c_p = 0
    c_q = 0
    c_r = 0
    c_s = 0
    c_t = 0
    c_u = 0
    c_v = 0
    c_w = 0
    c_x = 0
    c_y = 0
    c_z = 0

    # loop that runs for every character in string user_input
    for ch in user_input:
        # counts how many times a letter has occurred
        if ch == 'a':
            c_a += 1
        if ch == 'b':
            c_b += 1
        if ch == 'c':
            c_c += 1
        if ch == 'd':
            c_d += 1
        if ch == 'e':
            c_e += 1
        if ch == 'f':
            c_f += 1
        if ch == 'g':
            c_g += 1
        if ch == 'h':
            c_h += 1
        if ch == 'i':
            c_i += 1
        if ch == 'j':
            c_j += 1
        if ch == 'k':
            c_k += 1
        if ch == 'l':
            c_l += 1
        if ch == 'm':
            c_m += 1
        if ch == 'n':
            c_n += 1
        if ch == 'o':
            c_o += 1
        if ch == 'p':
            c_p += 1
        if ch == 'q':
            c_q += 1
        if ch == 'r':
            c_r += 1
        if ch == 's':
            c_s += 1
        if ch == 't':
            c_t += 1
        if ch == 'u':
            c_u += 1
        if ch == 'v':
            c_v += 1
        if ch == 'w':
            c_w += 1
        if ch == 'x':
            c_x += 1
        if ch == 'y':
            c_y += 1
        if ch == 'z':
            c_z += 1
    
    # checks to see what letter has occurred most frequently
    if c_a >= c_b and c_a >= c_c and c_a >= c_d and c_a >= c_e and c_a >= c_f and c_a >= c_g and c_a >= c_h and c_a >= c_i and c_a >= c_j and c_a >= c_k and c_a >= c_l and c_a >= c_m and c_a >= c_n and c_a >= c_o and c_a >= c_p and c_a >= c_q and c_a >= c_r and c_a >= c_s and c_a >= c_t and c_a >= c_u and c_a >= c_v and c_a >= c_w and c_a >= c_x and c_a >= c_y and c_a >= c_z:
        print("A appears most frequently,", c_a, "times.")
    if c_b >= c_a and c_b >= c_c and c_b >= c_d and c_b >= c_e and c_b >= c_f and c_b >= c_g and c_b >= c_h and c_b >= c_i and c_b >= c_j and c_b >= c_k and c_b >= c_l and c_b >= c_m and c_b >= c_n and c_b >= c_o and c_b >= c_p and c_b >= c_q and c_b >= c_r and c_b >= c_s and c_b >= c_t and c_b >= c_u and c_b >= c_v and c_b >= c_w and c_b >= c_x and c_b >= c_y and c_b >= c_z:
        print("B appears most frequently,", c_b, "times.")
    if c_c >= c_b and c_c >= c_a and c_c >= c_d and c_c >= c_e and c_c >= c_f and c_c >= c_g and c_c >= c_h and c_c >= c_i and c_c >= c_j and c_c >= c_k and c_c >= c_l and c_c >= c_m and c_c >= c_n and c_c >= c_o and c_c >= c_p and c_c >= c_q and c_c >= c_r and c_c >= c_s and c_c >= c_t and c_c >= c_u and c_c >= c_v and c_c >= c_w and c_c >= c_x and c_c >= c_y and c_c >= c_z:
        print("C appears most frequently,", c_c, "times.")
    if c_d >= c_b and c_d >= c_c and c_d >= c_a and c_d >= c_e and c_d >= c_f and c_d >= c_g and c_d >= c_h and c_d >= c_i and c_d >= c_j and c_d >= c_k and c_d >= c_l and c_d >= c_m and c_d >= c_n and c_d >= c_o and c_d >= c_p and c_d >= c_q and c_d >= c_r and c_d >= c_s and c_d >= c_t and c_d >= c_u and c_d >= c_v and c_d >= c_w and c_d >= c_x and c_d >= c_y and c_d >= c_z:
        print("D appears most frequently,", c_d, "times.")
    if c_e >= c_b and c_e >= c_c and c_e >= c_d and c_e >= c_a and c_e >= c_f and c_e >= c_g and c_e >= c_h and c_e >= c_i and c_e >= c_j and c_e >= c_k and c_e >= c_l and c_e >= c_m and c_e >= c_n and c_e >= c_o and c_e >= c_p and c_e >= c_q and c_e >= c_r and c_e >= c_s and c_e >= c_t and c_e >= c_u and c_e >= c_v and c_e >= c_w and c_e >= c_x and c_e >= c_y and c_e >= c_z:
        print("E appears most frequently,", c_e, "times.")
    if c_f >= c_b and c_f >= c_c and c_f >= c_d and c_f >= c_a and c_f >= c_e and c_f >= c_g and c_f >= c_h and c_f >= c_i and c_f >= c_j and c_f >= c_k and c_f >= c_l and c_f >= c_m and c_f >= c_n and c_f >= c_o and c_f >= c_p and c_f >= c_q and c_f >= c_r and c_f >= c_s and c_f >= c_t and c_f >= c_u and c_f >= c_v and c_f >= c_w and c_f >= c_x and c_f >= c_y and c_f >= c_z:
        print("F appears most frequently,", c_f, "times.")
    if c_g >= c_b and c_g >= c_c and c_g >= c_d and c_g >= c_a and c_g >= c_f and c_g >= c_e and c_g >= c_h and c_g >= c_i and c_g >= c_j and c_g >= c_k and c_g >= c_l and c_g >= c_m and c_g >= c_n and c_g >= c_o and c_g >= c_p and c_g >= c_q and c_g >= c_r and c_g >= c_s and c_g >= c_t and c_g >= c_u and c_g >= c_v and c_g >= c_w and c_g >= c_x and c_g >= c_y and c_g >= c_z:
        print("G appears most frequently,", c_g, "times.")
    if c_h >= c_b and c_h >= c_c and c_h >= c_d and c_h >= c_a and c_h >= c_f and c_h >= c_g and c_h >= c_e and c_h >= c_i and c_h >= c_j and c_h >= c_k and c_h >= c_l and c_h >= c_m and c_h >= c_n and c_h >= c_o and c_h >= c_p and c_h >= c_q and c_h >= c_r and c_h >= c_s and c_h >= c_t and c_h >= c_u and c_h >= c_v and c_h >= c_w and c_h >= c_x and c_h >= c_y and c_h >= c_z:
        print("H appears most frequently,", c_h, "times.")
    if c_i >= c_b and c_i >= c_c and c_i >= c_d and c_i >= c_a and c_i >= c_f and c_i >= c_g and c_i >= c_h and c_i >= c_e and c_i >= c_j and c_i >= c_k and c_i >= c_l and c_i >= c_m and c_i >= c_n and c_i >= c_o and c_i >= c_p and c_i >= c_q and c_i >= c_r and c_i >= c_s and c_i >= c_t and c_i >= c_u and c_i >= c_v and c_i >= c_w and c_i >= c_x and c_i >= c_y and c_i >= c_z:
        print("I appears most frequently,", c_i, "times.")
    if c_j >= c_b and c_j >= c_c and c_j >= c_d and c_j >= c_a and c_j >= c_f and c_j >= c_g and c_j >= c_h and c_j >= c_i and c_j >= c_e and c_j >= c_k and c_j >= c_l and c_j >= c_m and c_j >= c_n and c_j >= c_o and c_j >= c_p and c_j >= c_q and c_j >= c_r and c_j >= c_s and c_j >= c_t and c_j >= c_u and c_j >= c_v and c_j >= c_w and c_j >= c_x and c_j >= c_y and c_j >= c_z:
        print("J appears most frequently,", c_j, "times.")
    if c_k >= c_b and c_k >= c_c and c_k >= c_d and c_k >= c_a and c_k >= c_f and c_k >= c_g and c_k >= c_h and c_k >= c_i and c_k >= c_j and c_k >= c_e and c_k >= c_l and c_k >= c_m and c_k >= c_n and c_k >= c_o and c_k >= c_p and c_k >= c_q and c_k >= c_r and c_k >= c_s and c_k >= c_t and c_k >= c_u and c_k >= c_v and c_k >= c_w and c_k >= c_x and c_k >= c_y and c_k >= c_z:
        print("K appears most frequently,", c_k, "times.")
    if c_l >= c_b and c_l >= c_c and c_l >= c_d and c_l >= c_a and c_l >= c_f and c_l >= c_g and c_l >= c_h and c_l >= c_i and c_l >= c_j and c_l >= c_k and c_l >= c_e and c_l >= c_m and c_l >= c_n and c_l >= c_o and c_l >= c_p and c_l >= c_q and c_l >= c_r and c_l >= c_s and c_l >= c_t and c_l >= c_u and c_l >= c_v and c_l >= c_w and c_l >= c_x and c_l >= c_y and c_l >= c_z:
        print("L appears most frequently,", c_l, "times.")
    if c_m >= c_b and c_m >= c_c and c_m >= c_d and c_m >= c_a and c_m >= c_f and c_m >= c_g and c_m >= c_h and c_m >= c_i and c_m >= c_j and c_m >= c_k and c_m >= c_l and c_m >= c_e and c_m >= c_n and c_m >= c_o and c_m >= c_p and c_m >= c_q and c_m >= c_r and c_m >= c_s and c_m >= c_t and c_m >= c_u and c_m >= c_v and c_m >= c_w and c_m >= c_x and c_m >= c_y and c_m >= c_z:
        print("M appears most frequently,", c_m, "times.")
    if c_n >= c_b and c_n >= c_c and c_n >= c_d and c_n >= c_a and c_n >= c_f and c_n >= c_g and c_n >= c_h and c_n >= c_i and c_n >= c_j and c_n >= c_k and c_n >= c_l and c_n >= c_m and c_n >= c_e and c_n >= c_o and c_n >= c_p and c_n >= c_q and c_n >= c_r and c_n >= c_s and c_n >= c_t and c_n >= c_u and c_n >= c_v and c_n >= c_w and c_n >= c_x and c_n >= c_y and c_n >= c_z:
        print("N appears most frequently,", c_n, "times.")
    if c_o >= c_b and c_o >= c_c and c_o >= c_d and c_o >= c_a and c_o >= c_f and c_o >= c_g and c_o >= c_h and c_o >= c_i and c_o >= c_j and c_o >= c_k and c_o >= c_l and c_o >= c_m and c_o >= c_n and c_o >= c_e and c_o >= c_p and c_o >= c_q and c_o >= c_r and c_o >= c_s and c_o >= c_t and c_o >= c_u and c_o >= c_v and c_o >= c_w and c_o >= c_x and c_o >= c_y and c_o >= c_z:
        print("O appears most frequently,", c_o, "times.")
    if c_p >= c_b and c_p >= c_c and c_p >= c_d and c_p >= c_a and c_p >= c_f and c_p >= c_g and c_p >= c_h and c_p >= c_i and c_p >= c_j and c_p >= c_k and c_p >= c_l and c_p >= c_m and c_p >= c_n and c_p >= c_o and c_p >= c_e and c_p >= c_q and c_p >= c_r and c_p >= c_s and c_p >= c_t and c_p >= c_u and c_p >= c_v and c_p >= c_w and c_p >= c_x and c_p >= c_y and c_p >= c_z:
        print("P appears most frequently,", c_p, "times.")
    if c_q >= c_b and c_q >= c_c and c_q >= c_d and c_q >= c_a and c_q >= c_f and c_q >= c_g and c_q >= c_h and c_q >= c_i and c_q >= c_j and c_q >= c_k and c_q >= c_l and c_q >= c_m and c_q >= c_n and c_q >= c_o and c_q >= c_p and c_q >= c_e and c_q >= c_r and c_q >= c_s and c_q >= c_t and c_q >= c_u and c_q >= c_v and c_q >= c_w and c_q >= c_x and c_q >= c_y and c_q >= c_z:
        print("Q appears most frequently,", c_q, "times.")
    if c_r >= c_b and c_r >= c_c and c_r >= c_d and c_r >= c_a and c_r >= c_f and c_r >= c_g and c_r >= c_h and c_r >= c_i and c_r >= c_j and c_r >= c_k and c_r >= c_l and c_r >= c_m and c_r >= c_n and c_r >= c_o and c_r >= c_p and c_r >= c_q and c_r >= c_e and c_r >= c_s and c_r >= c_t and c_r >= c_u and c_r >= c_v and c_r >= c_w and c_r >= c_x and c_r >= c_y and c_r >= c_z:
        print("R appears most frequently,", c_r, "times.")
    if c_s >= c_b and c_s >= c_c and c_s >= c_d and c_s >= c_a and c_s >= c_f and c_s >= c_g and c_s >= c_h and c_s >= c_i and c_s >= c_j and c_s >= c_k and c_s >= c_l and c_s >= c_m and c_s >= c_n and c_s >= c_o and c_s >= c_p and c_s >= c_q and c_s >= c_r and c_s >= c_e and c_s >= c_t and c_s >= c_u and c_s >= c_v and c_s >= c_w and c_s >= c_x and c_s >= c_y and c_s >= c_z:
        print("S appears most frequently,", c_s, "times.")
    if c_t >= c_b and c_t >= c_c and c_t >= c_d and c_t >= c_a and c_t >= c_f and c_t >= c_g and c_t >= c_h and c_t >= c_i and c_t >= c_j and c_t >= c_k and c_t >= c_l and c_t >= c_m and c_t >= c_n and c_t >= c_o and c_t >= c_p and c_t >= c_q and c_t >= c_r and c_t >= c_s and c_t >= c_e and c_t >= c_u and c_t >= c_v and c_t >= c_w and c_t >= c_x and c_t >= c_y and c_t >= c_z:
        print("T appears most frequently,", c_t, "times.")
    if c_u >= c_b and c_u >= c_c and c_u >= c_d and c_u >= c_a and c_u >= c_f and c_u >= c_g and c_u >= c_h and c_u >= c_i and c_u >= c_j and c_u >= c_k and c_u >= c_l and c_u >= c_m and c_u >= c_n and c_u >= c_o and c_u >= c_p and c_u >= c_q and c_u >= c_r and c_u >= c_s and c_u >= c_t and c_u >= c_e and c_u >= c_v and c_u >= c_w and c_u >= c_x and c_u >= c_y and c_u >= c_z:
        print("U appears most frequently,", c_u, "times.")
    if c_v >= c_b and c_v >= c_c and c_v >= c_d and c_v >= c_a and c_v >= c_f and c_v >= c_g and c_v >= c_h and c_v >= c_i and c_v >= c_j and c_v >= c_k and c_v >= c_l and c_v >= c_m and c_v >= c_n and c_v >= c_o and c_v >= c_p and c_v >= c_q and c_v >= c_r and c_v >= c_s and c_v >= c_t and c_v >= c_u and c_v >= c_e and c_v >= c_w and c_v >= c_x and c_v >= c_y and c_v >= c_z:
        print("V appears most frequently,", c_v, "times.")
    if c_w >= c_b and c_w >= c_c and c_w >= c_d and c_w >= c_a and c_w >= c_f and c_w >= c_g and c_w >= c_h and c_w >= c_i and c_w >= c_j and c_w >= c_k and c_w >= c_l and c_w >= c_m and c_w >= c_n and c_w >= c_o and c_w >= c_p and c_w >= c_q and c_w >= c_r and c_w >= c_s and c_w >= c_t and c_w >= c_u and c_w >= c_v and c_w >= c_e and c_w >= c_x and c_w >= c_y and c_w >= c_z:
        print("W appears most frequently,", c_w, "times.")
    if c_x >= c_b and c_x >= c_c and c_x >= c_d and c_x >= c_a and c_x >= c_f and c_x >= c_g and c_x >= c_h and c_x >= c_i and c_x >= c_j and c_x >= c_k and c_x >= c_l and c_x >= c_m and c_x >= c_n and c_x >= c_o and c_x >= c_p and c_x >= c_q and c_x >= c_r and c_x >= c_s and c_x >= c_t and c_x >= c_u and c_x >= c_v and c_x >= c_w and c_x >= c_e and c_x >= c_y and c_x >= c_z:
        print("X appears most frequently,", c_x, "times.")
    if c_y >= c_b and c_y >= c_c and c_y >= c_d and c_y >= c_a and c_y >= c_f and c_y >= c_g and c_y >= c_h and c_y >= c_i and c_y >= c_j and c_y >= c_k and c_y >= c_l and c_y >= c_m and c_y >= c_n and c_y >= c_o and c_y >= c_p and c_y >= c_q and c_y >= c_r and c_y >= c_s and c_y >= c_t and c_y >= c_u and c_y >= c_v and c_y >= c_w and c_y >= c_x and c_y >= c_e and c_y >= c_z:
        print("Y appears most frequently,", c_y, "times.")
    if c_z >= c_b and c_z >= c_c and c_z >= c_d and c_z >= c_a and c_z >= c_f and c_z >= c_g and c_z >= c_h and c_z >= c_i and c_z >= c_j and c_z >= c_k and c_z >= c_l and c_z >= c_m and c_z >= c_n and c_z >= c_o and c_z >= c_p and c_z >= c_q and c_z >= c_r and c_z >= c_s and c_z >= c_t and c_z >= c_u and c_z >= c_v and c_z >= c_w and c_z >= c_x and c_z >= c_y and c_z >= c_e:
        print("Z appears most frequently,", c_z, "times.")

# run function main
main()
