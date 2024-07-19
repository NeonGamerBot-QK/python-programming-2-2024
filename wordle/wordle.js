Reset = "\x1b[0m"
Bright = "\x1b[1m"
Dim = "\x1b[2m"
Underscore = "\x1b[4m"
Blink = "\x1b[5m"
Reverse = "\x1b[7m"
Hidden = "\x1b[8m"

FgBlack = "\x1b[30m"
FgRed = "\x1b[31m"
FgGreen = "\x1b[32m"
FgYellow = "\x1b[33m"
FgBlue = "\x1b[34m"
FgMagenta = "\x1b[35m"
FgCyan = "\x1b[36m"
FgWhite = "\x1b[37m"
FgGray = "\x1b[90m"

BgBlack = "\x1b[40m"
BgRed = "\x1b[41m"
BgGreen = "\x1b[42m"
BgYellow = "\x1b[43m"
BgBlue = "\x1b[44m"
BgMagenta = "\x1b[45m"
BgCyan = "\x1b[46m"
BgWhite = "\x1b[47m"
BgGray = "\x1b[100m"
if(!process.env.TERM.includes('kitty')) {
    console.log(`Use Kitty Terminal app for better preformance`)
    process.exit(1)
}
const readLine = () => new Promise((r) => {
    process.stdin.once('data', d => r(d.toString()))
})

// mimic py functions
const get_word_list = () => {
    // for js one im doing random stuff
    return ['Tasco', 'Scalp', 'Tress', 'Folks'].map(w => w.toLowerCase().trim()).sort((a,b) => Math.random() > .5 ? 1 -2 : 2 - 1)
}
const pick_random_word = (list) => list[Math.floor(Math.random() * list.length)]

const color_letter = (letter, color) => `${color}${letter}${Reset}`
const evaluate_guess = (guess, secret_word) => {
    const words = []
    //Determine how many letters in the guess are in the secret word
    for(const letter of guess.split('')) {
     const lIndex = secret_word.indexOf(letter)
     if(lIndex >= 0) {
if(lIndex == guess.indexOf(letter)) {
    words.push(color_letter(letter, FgGreen))
} else {
    words.push(color_letter(letter, FgYellow))
}
     } else {
        words.push(color_letter(letter, FgGray))
     }
       
    }
    return words;
}
 function play_wordle() {
    console.log(`Starting wordle...`)
    const word = pick_random_word(get_word_list())
    if(process.env.REVEAL_WORD) console.log(`Cheater: ${word}`)
    // console.log(`Your wordle input`)
    let board = []
async function run(err) {
    console.log(new Array(40).join('='))
if(board.length > 0) {
    board.forEach(row => console.log(row.join(' ')))
} else {
    console.log('<empty board>')
}
    console.log(new Array(40).join('='))
    if(err) console.warn(err)
    process.stdout.write(`Enter your guess: `)
    const input = await readLine().then(str => str.replace(/[^a-zA-Z]+/g, '').slice(0, 5))
    if(input.length < 5) {
        // console.log(``)
        console.clear()
        return run("Make sure your guess is 5 Characters!");
    }
    const newRow =  evaluate_guess(input, word)
    if(board.length >= 5) {
        // console.log(board[board.length - 1])
        // const maybeWord = board[board.length - 1].join('').replaceAll(Reset, '').replaceAll(FgYellow, '').replaceAll(FgGray, '').replaceAll(FgGreen, '').trim()
        // console.log(`Does '${maybeWord}' == '${word}'`)
if(input == word) {
    console.log(`${FgGreen}You won??${Reset} `)
    setTimeout(() => process.exit(1), 50)
    return;
} else {
    console.log(`${FgRed} You Lost! ${Reset}`)
    setTimeout(() => process.exit(1), 50)
    return;
}
        return;
    } else {
    if(input == word) {
    console.log(`${FgGreen}You won??${Reset} `)
        // console.log(`You won??`)
        setTimeout(() => process.exit(1), 50)
        return;
    } else {
        board.push(newRow)
        console.clear()
        run()
    }
    }
}
run()
}
play_wordle()