var os = require('os-utils');
var xtea = require('xtea');
var plaintext = new Buffer('ABCDEFGH', 'utf8');
var key = new Buffer('0123456789ABCDEF0123456789ABCDEF', 'hex');
var ciphertext = xtea.encrypt( plaintext, key );
console.time("encryption");

console.log('Cipher:\t'+ ciphertext.toString('hex') );
console.time("decryption");
console.log('Decipher:\t'+ xtea.decrypt( ciphertext, key ).toString() );
console.timeEnd("decryption");
console.timeEnd("encryption");
console.time("encryption1000");
for (i = 0; i < 1000; i++) {

console.log('Cipher:\t'+ ciphertext.toString('hex') );
}
console.timeEnd("encryption1000");
console.time("decryption1000");
for (i = 0; i < 1000; i++) {
console.log('Decipher:\t'+ xtea.decrypt( ciphertext, key ).toString() );
}
console.timeEnd("decryption1000");
os.cpuUsage(function(v){
    console.log( 'CPU Usage (%): ' + v );
});
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
