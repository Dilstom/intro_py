function translate(phrase) {
    let translated = '';
    const vowels = 'AEOUIaeoui';
    for (letter in phrase) {
        // console.log(phrase[letter]);
        if (vowels.includes(phrase[letter])) {
            // if (phrase[letter] === phrase[letter].toUpperCase()) {
            //     translated += 'G';
            // }
            // else {
            //     translated += 'g';
            // }
            phrase[letter] === phrase[letter].toUpperCase() ? translated += 'G' : translated += 'g';
        } else {
            translated += phrase[letter];
        }

    }
    return translated;
}

translate(prompt("Enter a phrase: "));
