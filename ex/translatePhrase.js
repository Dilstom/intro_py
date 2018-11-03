function translate(phrase) {
    let translated = '';
    const vowels = 'AEOUIaeoui';
    for (letter in phrase) {
        // console.log(phrase[letter]);
        if (vowels.includes(phrase[letter])) {
            translated += 'g';
        } else {
            translated += phrase[letter];
        }
    }
    return translated;
}

translate('giraffe')