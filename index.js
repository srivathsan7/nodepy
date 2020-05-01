const express=require('express')
const app=express()
const {spawn}=require('child_process')
const port=process.env.PORT || 3000
app.use(express.json())
app.listen(port,() =>{
	console.log('server is up on port '+port)
})
var largeDataSet = []
app.get('/',(req,res)=>{
	const id='6'
	const python =spawn('python', ['content-based.py',id])
	python.stdout.on('data', function (data) {
  console.log('Pipe data from python script ...')
  largeDataSet.push(data);
 })
 python.on('close', (code) => {
 console.log(`child process close all stdio with code ${code}`)
 res.send(largeDataSet.join(""))
  })
})