import axios from 'axios'

export async function askAIQuesion(payload){
    try {
    console.log('api payload', payload)
        const response = await axios.get('http://127.0.0.1:5000/chat', payload)
    console.log('api response LOOKUP', response.data)
    return response.data
} catch (error) {
        console.log('api om null')
    }
}