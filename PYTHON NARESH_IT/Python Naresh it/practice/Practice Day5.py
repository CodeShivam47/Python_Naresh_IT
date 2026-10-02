# 1 => H1 — Sentiment Counter v2. Extend the lab: process at least 10 messages, add a MIXED category (contains both a positive and a negative word), and print all four totals plus which category is most common.
message = [
    " I love this service",
    "This is a bad experience",
    "The product is good but the support is terrible",
    "Amazing and helpful team",
    "I hate writing so long",
    "Great result, i am happy",
    "This is not good",
    "Excellent work",
    "Bad quality and poor performance",
    "I love it but the delay is awful"
]
positive_words = ["good","great", "love","happy","excellent","amazing","helpful"]
negative_words = ["bad","hate","terrible","poor", "awful","delay"]

totals ={
    "positive":0,
    "negetive":0,
    "mixed":0,
    "unknon":0
}
for msg in message:
    text = msg.lower()
    has_positive = False,
    has_negative = False
    for word in positive_words:
        if word in text:
            has_positive = True

    for word in negative_words:
        if word in text:
            has_negetive = True

        if has_positive and has_negative:
            category = "mixed"
        elif has_positive:
            category = "positive"
        elif has_negetive:
            category = "negetive"
        else:
            category = "unknown"
        totals[category] += 1
# print("positive:", totals["positive"]),
# print("Negetive:"), totals ["negetive"],
# print("mixed:"), totals ["mixed"],
# print("unknown:"), totals ["unknown"]

most_common = "unknown"
for category in totals:
    if totals[category] > totals[most_common]:
        most_common = category
        #print("most common category:",most_common)


# Q =>2 



