for (let i = 0; i < 3; i++) {
    console.log('first')
    setTimeout(() => console.log(i), 0); 
    console.log('last')
}