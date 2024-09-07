const screen = document.getElementsByClassName("testmonial-cards")[0];
const card = document.querySelector(".testmonial-cards .cards");

// scrollingleft funtion
const scrollleft = () => {
	screen.scrollLeft -= card.offsetWidth + 16;
};

// scrollingright funtion
const scrollright = () => {
	screen.scrollLeft += card.offsetWidth + 16;
};

// course cards price calculating

const courseCards = document.getElementsByClassName("course-price-details");

Array.from(courseCards).forEach((card) => {
	const mrp = parseFloat(card.dataset.mrp);
	const discountPercentage = parseFloat(card.dataset.discount);

	let coursePrice = mrp - mrp * (discountPercentage / 100);

	coursePrice = Math.round(coursePrice * 100) / 100;

	if (coursePrice === Math.floor(coursePrice)) {
		coursePrice = parseInt(coursePrice, 10);
	} else {
		coursePrice = parseFloat(coursePrice.toFixed(2));
	}

	const priceElement = card.querySelector(".course-details h4");

	if (priceElement) {
		priceElement.textContent = `$${coursePrice}`;
	} else {
		console.error("Price element not found in card:", card);
	}
});

//calculate course price

try {
	document.addEventListener("DOMContentLoaded", () => {
		const data = document.getElementsByClassName("pricebox");

		if (data) {
			Array.from(data).forEach((card) => {
				const mrp = parseFloat(card.dataset.mrp);
				const discountPercentage = parseFloat(card.dataset.discount);

				let coursePrice = mrp - mrp * (discountPercentage / 100);

				coursePrice = Math.round(coursePrice * 100) / 100;

				if (coursePrice === Math.floor(coursePrice)) {
					coursePrice = parseInt(coursePrice, 10);
				} else {
					coursePrice = parseFloat(coursePrice.toFixed(2));
				}

				const priceElement = card.querySelector(".price");
				console.log(priceElement);

				if (priceElement) {
					priceElement.textContent = `$${coursePrice}`;
				} else {
					console.error("Price element not found in card:", card);
				}
			});
		} else {
			console.log("not loaded");
		}
	});
} catch (error) {
	console.log("not loaded");
}
