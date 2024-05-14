from tkinter import *
from animatedGIF_class import *
from tkinter.font import Font
import random

def rgbToHex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

window = tk.Tk()
window.title("Heidi's food ideas")

width = 650
height = 670
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width - width) // 2
y = (screen_height - height) // 2

window.geometry(f"{width}x{height}+{x}+{y}")

window_bgColor_hex = rgbToHex(229,204,255)
window.configure(background=window_bgColor_hex)

photo = AnimatedGIF(window, "200w.gif", bg_color=window_bgColor_hex)

photo.pack()

add_font = ("Comic Sans MS", 15, "bold") 
add_fgColor_hex = rgbToHex(200,130,225)
add_label = Label(window, text="How hungry are you?", bg=window_bgColor_hex, \
                  fg=add_fgColor_hex, font=add_font)
add_label.pack()

textEntry = Entry(window, width=15, bg=window_bgColor_hex, \
                  fg=add_fgColor_hex, font=add_font)
textEntry.pack()

def click():
    foodOptionsDict = {
    1: {"Starbucks": {"2701 Harbor Blvd Ste D1, Costa Mesa, CA 92626", \
                      "3030 Harbor Blvd, Costa Mesa, CA 92626"}, \
        "IHOP": {"3125 Harbor Blvd, Costa Mesa, CA 92626", \
                 "18542 MacArthur Blvd, Irvine, CA 92612"}, \
        "Carl's Jr.": {"1550 Adams Ave, Costa Mesa, CA 92626", \
                       "3325 S Harbor Blvd, Santa Ana, CA 92704"}, \
        "The Habit Burger Grill": {"1510 Adams Ave, Costa Mesa, CA 92626"}, \
        "Benchmark": {"601 E Santa Ana Blvd, Santa Ana, CA 92701"},\
        "Solstice Seasonal Kitchen & Bar": {"18555 Jamboree Rd, Irvine, CA 92612"},\
        "Morrison Atwater Village (Burgers)": {"3179 Los Feliz Blvd, Los Angeles, CA 90039"}, \
        "Granville (Cocktail bars)": {"12345 Ventura Blvd, Studio City, CA 91604"}, \
        "Girl & The Goat": {"555-3 Mateo St, Los Angeles, CA 90013"}}, ## American
    2: {"Haidilao Hot Pot": {"2710 Alton Pkwy #215, Irvine, CA 92606"}, \
        "Capital Noodle Bar": {"3850 Barranca Pkwy Suite E, Irvine, CA 92606"}, \
        "Tim Ho Wan": {"2700 Alton Pkwy, Irvine, CA 92606"},\
        "Furiwa Togo": {"19530 Jamboree Rd, Irvine, CA 92612"}, \
        "Yijia (Porridge)": {"17881 Sky Park Circle, Irvine, CA 92614"}, \
        "Northeast Sisters": {"350 Clinton St, Costa Mesa, CA 92626"},\
        "Dun Huang": {"2710 Alton Pkwy #117, Irvine, CA 92606", \
                      "1370 Fullerton Rd #105, Rowland Heights, CA 91748"},\
        "Luyu Dumplings": {"17980 Castleton St, City of Industry, CA 91748"},\
        "Mountain House": {"18888 Labin Ct C101, Rowland Heights, CA 91748"}}, ## Chinese
    3: { "The India Cafe": { "528 W 19th St Costa Mesa, CA 92627" } }, ## Indian\
    4: { "Angelina's Pizzeria Napoletana": {"8573 Irvine Center Dr, Irvine, CA 92618"},\
         "ZeroZero39 Pizzeria": {"221 Main St D, Huntington Beach, CA 92648"}, \
         "Cosmo's Italian Kitchen": {"28562 Oso Pkwy # L, Rancho Santa Margarita, CA 92688"},\
         "Fatto a Mano The Pasta Shop": {"610 Torrance Blvd Redondo Beach, CA 90277"},\
         "Strada Eateria & Bar (Bars)": {"825 James M Wood Blvd #90015, Los Angeles, CA 90015"},\
         "Spaghettini": {"3005 Old Ranch Pkwy, Seal Beach, CA 90740"},\
         "Barrique": {"796 Main St, Venice, CA 90291"},\
         "Uovo": {"1320 2nd St Ste A, Santa Monica, CA 90401", \
                  "6245 Wilshire Blvd Suite 103, Los Angeles, CA 90048"} }, ## Italian\
         # "DAMA (Cocktail Bars)"  // Latin American 
    5: {"Izakaya Osen Irvine (Sushi Bars)": {"2000 Main St suite 100, Irvine, CA 92614"}, \
        "Umami Burger": {"527 Spectrum Center Dr, Irvine, CA 92618"}, \
        "Ricebunn Onigiri": {"Trade Food Hall, 2222 Michelson Dr #206, Irvine, CA 92612"}, \
        "Shinobu Japanese BBQ": {"15202 Goldenwest St, Westminster, CA 92683"},\
        "Yakiya (BBQ)": {"17188 Colima Rd, Hacienda Heights, CA 91745"}, \
        "San Shi Go (Sushi Bars)": {"205 Main St, Newport Beach, CA 92661"},\
        "Halves Boiling Pot + Grill (Shabu, BBQ)": {"45 Auto Center Dr #116, Foothill Ranch, CA 92610"}, \
        "Tsuruhashi": {"18798 Brookhurst St, Fountain Valley, CA 92708"}, \
        "Izakaya Hachi": {"3033 Bristol St D, Costa Mesa, CA 92626"},\
        "ROL Hand Roll Bar": {"16173 Brookhurst St, Fountain Valley, CA 92708",\
                              "7862 Warner Ave, Huntington Beach, CA 92647"},\
        "Hakata Ikkousha Tonkotsu Ramen": { "3033 Bristol St #131, Costa Mesa, CA 92626" }},## Japanese
    6: {"BCD Tofu House": {"2700 Alton Pkwy #135, Irvine, CA 92606"}, \
        "Chan Chan Food House": {"14250 Culver Dr, Irvine, CA 92604"}, \
        "JAWS TPK (Kimbap)": {"6924 Beach Blvd k335, Buena Park, CA 90621"}, \
        "Baekjeong (BBQ)": {"14160 Culver Dr, Irvine, CA 92604"}, \
        "Hanu Korean BBQ": {"2999 W 6th St #104, Los Angeles, CA 90020"}, \
        "Broken Mouth": {"718 S Los Angeles St, Los Angeles, CA 90014"},\
        "Yup Dduk LA": {"3603 W 6th St, Los Angeles, CA 90020"}, \
        "Mo Ran Gak Restaurant (BBQ)": {"9651 Garden Grove Blvd, Garden Grove, CA 92844"}, \
        "Woo Hyang Woo (BBQ)": {"3429 W 6th St, Los Angeles, CA 90020"}, \
        "Bon Tofu & Grill": {"17900 Magnolia St A, Fountain Valley, CA 92708"}}, ## Korean
    7: {"Avila's El Ranchito": {"2101 Placentia Ave, Costa Mesa, CA 92627"}, \
        "Tacos Madre Mexican Cocina": {"2629 Harbor Blvd, Costa Mesa, CA 92626"} }, ## Mexian
    8: {"Din Tai Fung": {"3333 Bristol St Ste Ste 2071, Costa Mesa, CA 92626"}, \
        "Four Sea Restaurant": {"15435 Jeffrey Rd, Irvine, CA 92618"}, \
        "Yi Mei Taiwanese Restaurant": {"3210 Chino Ave, Chino Hills, CA 91709"}, \
        "Meet Fresh": {"2710 Alton Pkwy #105, Irvine, CA 92606"},\
        "85 Bakery Cafe": {"2700 Alton Pkwy #123, Irvine, CA 92606"},\
        "A&J": {"14805 Jeffrey Rd, Irvine, CA 92618"}, \
        "Class 302 Taiwanese Cafe": {"13252 Jamboree Rd, Irvine, CA 92602"},\
        "Boiling Point": {"14140 Culver Dr, Irvine, CA 92604"}, \
        "Tasty House": {"827 W Las Tunas Dr, San Gabriel, CA 91776"}}, ## Taiwanese
    9: { "Phởholic": {"14932 Bushard St, Westminster, CA 92683"}, \
         "Pho Dakao": {"16171 Brookhurst St, Fountain Valley, CA 92708"},\
         "Carrot And Daikon Banh Mi": {"8511 Westminster Blvd., Garden Grove, CA 92844", \
                                       "9016 Bolsa Ave, Westminster, CA 92683"},\
         "Banh Khot Vung Tau": {"9110 Edinger Ave, Fountain Valley, CA 92708"},\
         "An Vat OC" : {"10021 Garden Grove Blvd, Garden Grove, CA 92844"},\
         "Com Tam Thanh": {"9870 Bolsa Ave, Westminster, CA 92683"},\
         "Khởi Hưng": {"10548 Westminster Ave, Garden Grove, CA 92843"},\
         "Nep Cafe by Kei Concepts": {"10836 Warner Ave Fountain Valley, CA 92708"}, 
         "Grandpa’s Kitchen Grill - Bar 168": {"14208 Brookhurst St, Garden Grove, CA 92843"},\
         "iLanet Coffee": {"13916 Brookhurst St, Garden Grove, CA 92843"}
         } 
         # "Ike's Love & Sandwiches": {"18529 Brookhurst St, Fountain Valley, CA 92708"} # Arabic Food
    }
    
    userSelected = sections_var.get()
    if userSelected == 10:
        userSelected = random.randint(1,9)
    restaurantsList = []
    for restaurantKey in foodOptionsDict[userSelected]:
        restaurantsList.append(restaurantKey)
    
    randomRastaurantKey = random.choice(restaurantsList)
    
    addressSet = foodOptionsDict[userSelected][randomRastaurantKey]
    randomAddress = random.choice(list(addressSet))   
   
    output.delete('1.0', END)
    output.insert(END, " " + randomRastaurantKey)
    
    addressOutput.delete('1.0', END)
    addressOutput.insert(END, " " + randomAddress)    
    
label_font = ("Comic Sans MS", 15, "bold")
sctnLabel_fgColor_hex = rgbToHex(173,121,225)

section_label = Label(window, text="What type of food are you feeling right now? "\
                      , bg=window_bgColor_hex, fg=sctnLabel_fgColor_hex, font=label_font)

section_label.pack()

radio_font = ("Comic Sans MS", 15, "bold")  
radio_fgColor_hex = rgbToHex(240,109,166)
sections_var = IntVar()

radio1 = Radiobutton(window, text="American Food", font=radio_font, \
                     fg=radio_fgColor_hex, bg=window_bgColor_hex, \
                     variable=sections_var, value=1)
radio2 = Radiobutton(window, text="Chinese Food", font=radio_font, \
                     fg=radio_fgColor_hex, bg=window_bgColor_hex, \
                     variable=sections_var, value=2)
radio3 = Radiobutton(window, text="Indian Food", font=radio_font, \
                     fg=radio_fgColor_hex, bg=window_bgColor_hex, \
                     variable=sections_var, value=3)
radio4 = Radiobutton(window, text="Italian Food", font=radio_font, \
                     fg=radio_fgColor_hex, bg=window_bgColor_hex, \
                     variable=sections_var, value=4)
radio5 = Radiobutton(window, text="Japanese Food", font=radio_font, \
                     fg=radio_fgColor_hex, bg=window_bgColor_hex, \
                     variable=sections_var, value=5)
radio6 = Radiobutton(window, text="Korean Food", font=radio_font, \
                     fg=radio_fgColor_hex, bg=window_bgColor_hex, \
                     variable=sections_var, value=6)
radio7 = Radiobutton(window, text="Mexican Food", font=radio_font, \
                     fg=radio_fgColor_hex, bg=window_bgColor_hex, \
                     variable=sections_var, value=7)
radio8 = Radiobutton(window, text="Taiwanese Food", font=radio_font, \
                     fg=radio_fgColor_hex, bg=window_bgColor_hex, \
                     variable=sections_var, value=8)
radio9 = Radiobutton(window, text="Vietnamese Food", font=radio_font, \
                     fg=radio_fgColor_hex, bg=window_bgColor_hex, \
                     variable=sections_var, value=9)
radio10 = Radiobutton(window, text="just tell me", font=radio_font, \
                     fg=radio_fgColor_hex, bg=window_bgColor_hex, \
                     variable=sections_var, value=10)

radio1.place(x=140, y=300)
radio2.place(x=140, y=340)
radio3.place(x=140, y=380)
radio4.place(x=140, y=420)
radio5.place(x=140, y=460)

radio6.place(x=360, y=300)
radio7.place(x=360, y=340)
radio8.place(x=360, y=380)
radio9.place(x=360, y=420)
radio10.place(x=360, y=460)

button_font = ("Comic Sans MS", 15, "bold")
submit_button = Button(window, text="Accio", font=button_font, width=3, \
                       height=1, command=click)
submit_button.place(x=294, y=510)

text_font = Font(family="Comic Sans MS", size=14, weight="bold") 
text_fgColor_hex = rgbToHex(102,102,102) 
text_bgColor_hex = rgbToHex(255,204,229)

output = Text(window, font=text_font, width=41, height=1, bg=text_bgColor_hex,\
              fg=text_fgColor_hex, insertbackground = "white") 
output.place(x=146, y=550)


addressOutput = Text(window, font=text_font, width=41, height=1, bg=text_bgColor_hex,\
              fg=text_fgColor_hex, insertbackground = "white") 

addressOutput.place(x=146, y=580)

window.mainloop()
