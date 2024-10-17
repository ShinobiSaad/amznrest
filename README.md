## Documentation

This application is a web scraper designed to extract watch data from Amazon. It utilizes Flask to manage the REST API, enabling efficient data retrieval and interaction.

## Installation

**Database**

```

docker-compose up -d

```

**Migration**

```

flask --app main.py db migrate -m <MESSAGE>

flask --app main.py db upgrade

```

**Run the scraper**

> **Note:** Use a separate terminal from running the Flask App.

```

python amazon_scraper.py

```

**Run the Flask App**

> **Note:** Use a separate terminal from running the scraper.

```

python main.py

```

## API DOCS

**1. Get All Products**

```
[GET]/products
```

> **Example URL**

```
http://127.0.0.1:5000/api/products
```

> **Response**

```
{
	"brand":  "Amazon Essentials Men's Easy to Read Strap Watch",
	"id":  34,
	"model":  "Amazon Essentials Men's Easy to Read Strap Watch ",
	"price":  16.0,
	"ratings":  "4.4",
	"specifications":  "STYLE: A classic, easy-to-read timepiece for everyday wear; 42mm case; band length 9.5 inches\nMATERIAL: Brown faux leather strap with genuine leather backing for comfortable wear; buckle closure; mineral crystal lens\nDETAILS: Matte white dial with gold tone luminous hands and easy to read black Arabic numerals; printed outer minute track; date calendar window at 3 o'clock\nCARE: Water resistant to 100 Feet (30m); watches should be treated like jewelry; to best protect your watch, be sure to be conscious when spraying perfume, hair spray, etc.; a jewelry polishing cloth can be used to polish the watch and clean it of fingerprints\n"
},
{

	"brand":  "Amazon's Choice: Overall Pick",
	"id":  35,
	"model":  "Michael Kors Oversized Slim Runway Men's Watch, Stainless Steel Watch for Men ",
	"price":  95.0,
	"ratings":  "4.7",
	"specifications":  "The black IP Michael Kors Slim Runway watch is polished perfection. A classic three-link bracelet and monochromatic sunray dial with stick indexes add up to a wear-with-everything timepiece that dresses up and down with ease.\nCase & Dial: Round 44mm stainless steel case with a black dial; mineral crystal face resists scratches\nWatch Band: Black stainless steel bracelet band; 22mm band width; links can be removed for a customized fit\nMovement: Quartz movement with three-hand analog display; imported\nWater Resistant: Up to 50m (165ft): Wearable while swimming in shallow water; 5 ATM\n"

},
```

**1.1. Search by Brand**

```
[GET]/products?brand=
```

> **Example URL**

```
http://127.0.0.1:5000/api/products?brand=Fossil
```

> **Response**

```
{
	"brand":  "Fossil Grant Men's Watch with Chronograph or Automatic Display and Genuine Leather or Stainless Steel Band",
	"id":  42,
	"model":  "Fossil Grant Men's Watch with Chronograph or Automatic Display and Genuine Leather or Stainless Steel Band ",
	"price":  124.0,
	"ratings":  "4.6",
	"specifications":  "Sleek, self-winding and styled to tick on time with a built-in rotor, our Grant does the work for you. This timeless automatic gets refreshed for the season with a refined dial and rich leather strap. (No batteries required with a 40-hour power reserve.)\nCase & Movement: 45mm case, 22mm band width, hardened mineral crystal lens resists scratches, accurate Automatic movement with accurate Automatic analog display, imported.\nDial: Round silver stainless steel case, with a cream sunray and skeleton dial and black accents.\nWatch Band: Brown, genuine leather band with a secure adjustable buckle closure for a customized fit; interchangeable with all 22mm Fossil watch straps.\nWater Resistant: Up to 50m (165ft): Wearable for short periods of recreational swimming and showering, but not diving or snorkeling; 5 ATM.\nAn automatic—or self-winding—watch is a mechanical timepiece in which the mainspring is wound automatically from natural motion, making a battery unnecessary. If your watch has stopped, rotate crown clockwise approx 40 times.\n"
},
{
	"brand":  "Fossil Nate Men's Watch with Oversized Chronograph Watch Dial and Stainless Steel or Leather Band",
	"id":  44,
	"model":  "Fossil Nate Men's Watch with Oversized Chronograph Watch Dial and Stainless Steel or Leather Band ",
	"price":  97.0,
	"ratings":  "4.5",
	"specifications":  "From an inky matte dial to brushed jet steel, Nate gives the all-black trend new depth. Use it to dress up your favorite pair of denim and a crisp, white tee. This Nate watch also features a chronograph movement on a stainless steel bracelet.\nCase & Movement: 50mm case, 24mm band width, hardened mineral crystal lens resists scratches, accurate Quartz movement with chronograph analog display and date window, three subdials to track minutes, seconds, and 24-hour time, stopwatch functionality, imported.\nDial: Round black stainless steel case, with a black matte dial and gray accents.\nWatch Band: Black, durable stainless steel bracelet band with a secure fold-over clasp closure; links can be removed for a customized fit; interchangeable with all Fossil 24mm watch straps.\nWater Resistant: Up to 50m (165ft): Wearable for short periods of recreational swimming and showering, but not diving or snorkeling; 5 ATM.\n"
},
```

**1.2. Filter by Price**

```
[GET]/products?min_price=&max_price=
```

> **Example URL**

```
http://127.0.0.1:5000/api/products?min_price=50&max_price=150
```

> **Response**

```
{
	"brand":  "Amazon's Choice: Overall Pick",
	"id":  35,
	"model":  "Michael Kors Oversized Slim Runway Men's Watch, Stainless Steel Watch for Men ",
	"price":  95.0,
	"ratings":  "4.7",
	"specifications":  "The black IP Michael Kors Slim Runway watch is polished perfection. A classic three-link bracelet and monochromatic sunray dial with stick indexes add up to a wear-with-everything timepiece that dresses up and down with ease.\nCase & Dial: Round 44mm stainless steel case with a black dial; mineral crystal face resists scratches\nWatch Band: Black stainless steel bracelet band; 22mm band width; links can be removed for a customized fit\nMovement: Quartz movement with three-hand analog display; imported\nWater Resistant: Up to 50m (165ft): Wearable while swimming in shallow water; 5 ATM\n"
},
{
	"brand":  "Fossil Grant Men's Watch with Chronograph or Automatic Display and Genuine Leather or Stainless Steel Band",
	"id":  42,
	"model":  "Fossil Grant Men's Watch with Chronograph or Automatic Display and Genuine Leather or Stainless Steel Band ",
	"price":  124.0,
	"ratings":  "4.6",
	"specifications":  "Sleek, self-winding and styled to tick on time with a built-in rotor, our Grant does the work for you. This timeless automatic gets refreshed for the season with a refined dial and rich leather strap. (No batteries required with a 40-hour power reserve.)\nCase & Movement: 45mm case, 22mm band width, hardened mineral crystal lens resists scratches, accurate Automatic movement with accurate Automatic analog display, imported.\nDial: Round silver stainless steel case, with a cream sunray and skeleton dial and black accents.\nWatch Band: Brown, genuine leather band with a secure adjustable buckle closure for a customized fit; interchangeable with all 22mm Fossil watch straps.\nWater Resistant: Up to 50m (165ft): Wearable for short periods of recreational swimming and showering, but not diving or snorkeling; 5 ATM.\nAn automatic—or self-winding—watch is a mechanical timepiece in which the mainspring is wound automatically from natural motion, making a battery unnecessary. If your watch has stopped, rotate crown clockwise approx 40 times.\n"
},
```

**1.3. Filter by Ratings**

```
[GET]/products?min_rating=&max_rating=
```

> **Example URL**

```
http://127.0.0.1:5000/api/products?min_rating=4.7&max_rating=5
```

> **Response**

```
{
	"brand":  "Casio Men's MDV106-1AV 200 M WR Black Dive Watch (MDV106-1A)",
	"id":  48,
	"model":  "Casio Men's MDV106-1AV 200 M WR Black Dive Watch (MDV106-1A) ",
	"price":  52.0,
	"ratings":  "4.7",
	"specifications":  "Band Size: mens-standard\n"
},
{
	"brand":  "Casio Men's Classic Stainless Steel Japanese-Quartz Stainless-Steel Strap, Silver, 21 Casual Watch (Model: AE1200WHD-1A)",
	"id":  54,
	"model":  "Casio Men's Classic Stainless Steel Japanese-Quartz Stainless-Steel Strap, Silver, 21 Casual Watch (Model: AE1200WHD-1A) ",
	"price":  33.0,
	"ratings":  "4.7",
	"specifications":  "Lcd analog and digital display; world map and world time indicator\nLed light with afterglow; 5 daily alarms\n1/100th sec stopwatch; countdown timer\n12/24 hour formats; mute function\nWater-resistant to 100 M (330 feet)\n"
},
```

**1.4. Sort by Price Ascending**

```
[GET]/products?sort=
```

> **Example URL**

```
http://127.0.0.1:5000/api/products?sort=asc
```

> **Response**

```

{
	"brand":  "Casio Men's MQ24-7B2 Analog Black Resin Strap Watch",
	"id":  53,
	"model":  "Casio Men's MQ24-7B2 Analog Black Resin Strap Watch ",
	"price":  15.0,
	"ratings":  "4.4",
	"specifications":  "Round watch with logoed white dial featuring Arabic numeral markers\n35 mm plastic case with protective resin glass dial window\nQuartz movement with analog display\nBlack resin band with buckle closure\nwater resistant\n"
},
{
	"brand":  "Amazon Essentials Men's Easy to Read Strap Watch",
	"id":  34,
	"model":  "Amazon Essentials Men's Easy to Read Strap Watch ",
	"price":  16.0,
	"ratings":  "4.4",
	"specifications":  "STYLE: A classic, easy-to-read timepiece for everyday wear; 42mm case; band length 9.5 inches\nMATERIAL: Brown faux leather strap with genuine leather backing for comfortable wear; buckle closure; mineral crystal lens\nDETAILS: Matte white dial with gold tone luminous hands and easy to read black Arabic numerals; printed outer minute track; date calendar window at 3 o'clock\nCARE: Water resistant to 100 Feet (30m); watches should be treated like jewelry; to best protect your watch, be sure to be conscious when spraying perfume, hair spray, etc.; a jewelry polishing cloth can be used to polish the watch and clean it of fingerprints\n"
},
```

**1.5 Sort by Price Descending**

```
[GET]/products?sort=
```

> **Example URL**

```
http://127.0.0.1:5000/api/products?sort=desc
```

> **Response**

```
{
	"brand":  "Movado Men's Bold Verso Swiss Quartz Watch with Stainless Steel Strap, Gold Plated, 21.95 (Model: 3600866)",
	"id":  69,
	"model":  "Movado Men's Bold Verso Swiss Quartz Watch with Stainless Steel Strap, Gold Plated, 21.95 (Model: 3600866) ",
	"price":  746.0,
	"ratings":  "4.4",
	"specifications":  "COMPOSURE AND STYLE: Movado BOLD innovation meets modern design, time with a new attitude.\nRESILIENT DESIGN: Movado BOLD Verso Chronograph, 44 mm yellow gold ion-plated stainless steel case and bracelet with tachymeter scale. Features a yellow gold chronograph dial, Swiss Super-LumiNova accents, and date window detailing.\nREFINED SWISS ENGINEERING: Quartz watch movement is powered by a battery that charges and runs the watch. A Chronograph type of watch that is used as a stopwatch combined with a display watch. A basic chronograph has an independent sweep second hand; it can be started, stopped, and returned to zero by successive pressure on the stem.\nK1 MINERAL CRYSTAL GLASS: K1 mineral crystal is the most common crystal used in designer watches and more scratch-resistant than regular mineral crystal—and is even more shatter-resistant than sapphire crystal\nCARING FOR YOUR TIMEPIECE: Like any finely crafted mechanism, your Movado watch requires periodic maintenance to ensure optimal performance. A maintenance interval of 3 to 5 years is recommended, in addition to any required battery replacement. Never open the watch yourself.\n"
},
{
	"brand":  "Bulova Men's Archive Series Lunar Pilot 6-Hand Chronograph High Performance Quartz Stainless Steel, Black NATO Strap and Sapphire Crystal Style: 96A225",
	"id":  77,
	"model":  "Bulova Men's Archive Series Lunar Pilot 6-Hand Chronograph High Performance Quartz Stainless Steel, Black NATO Strap and Sapphire Crystal Style: 96A225 ",
	"price":  361.0,
	"ratings":  "4.7",
	"specifications":  "From the Bulova Archive Series, The Lunar Pilot made space history on August 2, 1971--during the Apollo 15 mission, a moon pilot chronograph was worn on the moon.\n6 Hand, Chronograph, High Performance Quartz\nSilver-Tone Stainless Steel and Black Nylon Stra\nSapphire Crystal\n50M Water Resistant and 3 Year Limited Warranty\n"
},
```

**1.6 Sort by Ratings Ascending**

```
[GET]/products?sort=
```

> **Example URL**

```
http://127.0.0.1:5000/api/products?sort=rating_asc
```

> **Response**

```
{
	"brand":  "IOWODO Smart Watch for Men Women - 1.85''HD Screen with Make and Answer Calls, with AI Voice Assistant, SpO2/Heart Rate/Sleep Monitor, 100+ Sports Modes, Smartwatch for Android and iOS (2 Straps)",
	"id":  52,
	"model":  "IOWODO Smart Watch for Men Women - 1.85''HD Screen with Make and Answer Calls, with AI Voice Assistant, SpO2/Heart Rate/Sleep Monitor, 100+ Sports Modes, Smartwatch for Android and iOS (2 Straps) ",
	"price":  28.0,
	"ratings":  "4.3",
	"specifications":  ""
},
{
	"brand":  "Timex Men's Expedition Scout 43mm Watch – Black Dial & Case with Brown Leather Strap",
	"id":  64,
	"model":  "Timex Men's Expedition Scout 43mm Watch – Black Dial & Case with Brown Leather Strap ",
	"price":  35.0,
	"ratings":  "4.4",
	"specifications":  "Adjustable brown 20mm genuine leather strap fits up to 8-inch wrist circumference\nBlack dial with date window at 3 o'clock; full Arabic numerals\nBlack 43mm brass case with mineral glass crystal\nIndiglo light-up watch dial; luminous hands\nWater resistant to 50m (165 ft): In general, suitable for short periods of recreational swimming, but not diving or snorkeling\n"
},
```

**1.7 Sort by Ratings Descending**

```
[GET]/products?sort=
```

> **Example URL**

```
http://127.0.0.1:5000/api/products?sort=rating_desc
```

> **Response**

```
{
	"brand":  "Fossil Copeland Men's Watch with Slim Case and Genuine Leather Band",
	"id":  61,
	"model":  "Fossil Copeland Men's Watch with Slim Case and Genuine Leather Band ",
	"price":  70.0,
	"ratings":  "4.7",
	"specifications":  "This 42mm Copeland features a blue sunray dial with Roman numeral and stick indices, three-hand movement and a luggage leather strap. Inspired by classic, turn-of-the-century wrist watches, Copeland is a minimalist take on the simplicity of a classic wirelug case. The sophisticated dial makes this a versatile timepiece for both casual and dress styles.\nCase & Movement: 42mm case, 22mm band width, hardened mineral crystal lens resists scratches, accurate Quartz movement with 3-hand analog display, imported.\nDial: Round silver stainless steel case, with a blue sunray dial and gold accents.\nWatch Band: Brown, genuine leather cuff band with a secure adjustable buckle closure for a customized fit.\nWater Resistant: Up to 50m (165ft): Wearable for short periods of recreational swimming and showering, but not diving or snorkeling; 5 ATM.\n"
},
{
	"brand":  "Anne Klein Women's Bracelet Watch",
	"id":  47,
	"model":  "Anne Klein Women's Bracelet Watch ",
	"price":  28.0,
	"ratings":  "4.6",
	"specifications":  "Mineral crystal lens\nGlossy black dial with gold-tone hands and markers\nGold-tone adjustable link bracelet; jewelry clasp and extender link\nInner bracelet circumference: 7 inches\nCase Diameter: 24mm\nWater resistant to 30 meters (99 feet): In general, withstands splashes or brief immersion in water, but not suitable for swimming or bathing\n"
}
```

**1.8 Pagination**

Default pagination is set and also customizable with endpoint

```
[GET]/products?page=&limit=
```

> **Example URL**

```
http://127.0.0.1:5000/api/products?page=1&limit=1
```

> **Response**

```
{
"products":  [
		{
		"brand":  "Amazon Essentials Men's Easy to Read Strap Watch",
		"id":  34,
		"model":  "Amazon Essentials Men's Easy to Read Strap Watch ",
		"price":  16.0,
		"ratings":  "4.4",
		"specifications":  "STYLE: A classic, easy-to-read timepiece for everyday wear; 42mm case; band length 9.5 inches\nMATERIAL: Brown faux leather strap with genuine leather backing for comfortable wear; buckle closure; mineral crystal lens\nDETAILS: Matte white dial with gold tone luminous hands and easy to read black Arabic numerals; printed outer minute track; date calendar window at 3 o'clock\nCARE: Water resistant to 100 Feet (30m); watches should be treated like jewelry; to best protect your watch, be sure to be conscious when spraying perfume, hair spray, etc.; a jewelry polishing cloth can be used to polish the watch and clean it of fingerprints\n"
		}
	]
}
```

**2. Get the Top Products**

```
[GET]/products/top
```

> **Example URL**

```
http://127.0.0.1:5000/api/products/top
```

> **Response**

```
{
	"brand":  "Amazon Essentials Men's Easy to Read Strap Watch",
	"id":  34,
	"image_url":  "https://amazon.com/sspa/click?ie=UTF8&spc=MTo0MTY1ODE2MDgyNzk1NDQ5OjE3MjkxNDExNTc6c3BfYXRmOjIwMDAyMDE3MjI5NzUzMTo6MDo6&url=%2FAmazon-Essentials-Gold-Tone-Brown-Strap%2Fdp%2FB07YQFY57B%2Fref%3Dsr_1_1_ffob_sspa%3Fdib%3DeyJ2IjoiMSJ9.PEM7L3YpTrScYlszuA2cWj8nP2RWOxithFWDYxoz1dwoXUbjBHQE50j9P4whBXTcA45qy_JW0MA7EVp2uj2E-L8iEYPzuI6EfoFhekqNpvev9SdAtqOy-RnokzHlklMWgodyQSHzIgSpbzqVDGZxXycFO7O6wqRvHoGlar29zq0PJRhKI53sGju0dF1u-lGkRzCKLAy_1c_5OhkiUUV7T7lHE6GIiqrRg8-kjpIS0I-knwtr2qhlLrCRlg0yVtBGLK8VTsBN-hitJhWTXuzKs5hEp_neNrPTIdSKivBg0lw.DRMc8BG6s8X8tgpf9jZkSh-VfbYwviAgpDjQTdDYARo%26dib_tag%3Dse%26keywords%3Dwatches%26qid%3D1729141157%26sr%3D8-1-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1",
	"model":  "Amazon Essentials Men's Easy to Read Strap Watch ",
	"price":  16.0,
	"ratings":  "4.4",
	"specifications":  "STYLE: A classic, easy-to-read timepiece for everyday wear; 42mm case; band length 9.5 inches\nMATERIAL: Brown faux leather strap with genuine leather backing for comfortable wear; buckle closure; mineral crystal lens\nDETAILS: Matte white dial with gold tone luminous hands and easy to read black Arabic numerals; printed outer minute track; date calendar window at 3 o'clock\nCARE: Water resistant to 100 Feet (30m); watches should be treated like jewelry; to best protect your watch, be sure to be conscious when spraying perfume, hair spray, etc.; a jewelry polishing cloth can be used to polish the watch and clean it of fingerprints\n"
},
{
	"brand":  "Amazon's Choice: Overall Pick",
	"id":  35,
	"image_url":  "https://amazon.com/Michael-Kors-Runway-Black-MK8507/dp/B01HEVAPSO/ref=sr_1_2?dib=eyJ2IjoiMSJ9.PEM7L3YpTrScYlszuA2cWj8nP2RWOxithFWDYxoz1dwoXUbjBHQE50j9P4whBXTcA45qy_JW0MA7EVp2uj2E-L8iEYPzuI6EfoFhekqNpvev9SdAtqOy-RnokzHlklMWgodyQSHzIgSpbzqVDGZxXycFO7O6wqRvHoGlar29zq0PJRhKI53sGju0dF1u-lGkRzCKLAy_1c_5OhkiUUV7T7lHE6GIiqrRg8-kjpIS0I-knwtr2qhlLrCRlg0yVtBGLK8VTsBN-hitJhWTXuzKs5hEp_neNrPTIdSKivBg0lw.DRMc8BG6s8X8tgpf9jZkSh-VfbYwviAgpDjQTdDYARo&dib_tag=se&keywords=watches&qid=1729141157&sr=8-2",
	"model":  "Michael Kors Oversized Slim Runway Men's Watch, Stainless Steel Watch for Men ",
	"price":  95.0,
	"ratings":  "4.7",
	"specifications":  "The black IP Michael Kors Slim Runway watch is polished perfection. A classic three-link bracelet and monochromatic sunray dial with stick indexes add up to a wear-with-everything timepiece that dresses up and down with ease.\nCase & Dial: Round 44mm stainless steel case with a black dial; mineral crystal face resists scratches\nWatch Band: Black stainless steel bracelet band; 22mm band width; links can be removed for a customized fit\nMovement: Quartz movement with three-hand analog display; imported\nWater Resistant: Up to 50m (165ft): Wearable while swimming in shallow water; 5 ATM\n"
},
```

**3. Get all reviews for a specific product**

```
[GET]/products/{product_id}/reviews
```

> **Example URL**

```
http://127.0.0.1:5000/api/products/35/reviews
```

> **Response**

```
{
"reviews":  [
		{
			"rating":  5.0,
			"review_date":  "Reviewed in the United States on October 4, 2024",
			"review_text":  "This appears to be a high quality product with a high quality look and feel. Yes, it's affordable. The watch is a very nice formal work watch.",
			"reviewer_name":  "Dudley Lightsey"
		},
		{
			"rating":  5.0,
			"review_date":  "Reviewed in the United States on September 14, 2024",
			"review_text":  "Honestly haven’t been into watches for very long but when it comes to them or anything else I love the modern look and compared to any other watch I own this is honestly my favorite. And I have a habit of dropping watches and so far this one is the most durable I don’t even see a scratch lol",
			"reviewer_name":  "Adam a."
		},
		{
			"rating":  5.0,
			"review_date":  "Reviewed in the United States on September 24, 2024",
			"review_text":  "I’m not a watch person but my spouse is. I got this for his birthday, to match my purse 😆 I thought it was very slimline and elegant, not bulky looking with all the unnecessary bells and whistles like many watches nowadays. And for the price, it looks really great! Hubby liked it too so thumbs up!",
			"reviewer_name":  "Kris"
		},
		{
			"rating":  5.0,
			"review_date":  "Reviewed in the United States on August 6, 2024",
			"review_text":  "As usual Michael Kors watch's do not disappoint. This watch is casual enough to wear to work or nice enough to wear out to any occasion. I had to have it resized but that is normal for me to have a link removed. look is sleek and the Black Stainless looks amazing.",
			"reviewer_name":  "Mark E."
		},
		{
			"rating":  5.0,
			"review_date":  "Reviewed in the United States on August 24, 2024",
			"review_text":  "My husband just loved this watch! The black face makes it pop! The gold band I ordered looks so nice with the face! Great value!",
			"reviewer_name":  "Theresa Boedeker"
		},
		{
			"rating":  4.0,
			"review_date":  "Reviewed in the United States on September 27, 2024",
			"review_text":  "Really good and its price is very good. It still works with me and its black color is very attractive.",
			"reviewer_name":  "Amazon Customer"
		},
		{
			"rating":  5.0,
			"review_date":  "Reviewed in the United States on September 9, 2024",
			"review_text":  "Classy and great for work. My boyfriend loves how the watch completes his business look. He said it is a little loose on his wrist but other than that he loves it.",
			"reviewer_name":  "Jenna G."
		},
		{
			"rating":  5.0,
			"review_date":  "Reviewed in the United States on July 29, 2024",
			"review_text":  "I bought this for my baby dad for Father’s Day and he loves it. It was a little big so he had to get a link removed but other than that very nice quality and very elegant looking.",
			"reviewer_name":  "Nicole Beckham"
		},
		{
			"rating":  5.0,
			"review_date":  "Reviewed in Mexico on July 30, 2024",
			"review_text":  "Es un telón muy bonito, llegó muy rápido y en excelente estado",
			"reviewer_name":  "Muy bueno el producto, muy cómodo, llegó en perfecto estado y rápido "
		},
		{
			"rating":  5.0,
			"review_date":  "Reviewed in Mexico on May 29, 2024",
			"review_text":  "Me encanto, muy buena compra y es idéntico a la foto. Lo recomiendo",
			"reviewer_name":  "Diego Alexei "
		}
	]
}
```

**3.1 Pagination on the review**

Default pagination is set and also customizable with endpoint

```
[GET]/products/{product_id}/reviews?page=&limit=
```

> **Example URL**

```
http://127.0.0.1:5000/api/products/35/reviews?page=1&limit=1
```

> **Response**

```
{
"reviews":  [
		{
			"rating":  5.0,
			"review_date":  "Reviewed in the United States on October 4, 2024",
			"review_text":  "This appears to be a high quality product with a high quality look and feel. Yes, it's affordable. The watch is a very nice formal work watch.",
			"reviewer_name":  "Dudley Lightsey"
		}
	]
}
```
