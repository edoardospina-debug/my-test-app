import React, { useState } from 'react';
   import axios from 'axios';
   import './App.css';

   const App: React.FC = () => {
     const [message, setMessage] = useState<string>('Click to fetch data');
     const [error, setError] = useState<string | null>(null);

     const fetchData = async () => {
       try {
         const response = await axios.get('/api/');
         setMessage(response.data.message);
       } catch (err) {
         setError('Failed to fetch data from the backend');
       }
     };

     return (
       <div className="min-h-screen bg-gray-100 flex items-center justify-center">
         <div className="bg-white p-6 rounded-lg shadow-lg">
           <h1 className="text-2xl font-bold mb-4">My FastAPI + React App</h1>
           {error ? (
             <p className="text-red-500">{error}</p>
           ) : (
             <p className="text-gray-700">{message}</p>
           )}
           <p className="text-blue-500">Test Tailwind class</p>
           <button
             className="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
             onClick={fetchData}
           >
             Fetch Message
           </button>
         </div>
       </div>
     );
   };

   export default App;