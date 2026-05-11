process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.setEncoding('utf8');
process.stdin.on('data', (chunk) => {
  process.stdout.write(`Your name is: ${chunk}`);
});

process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
