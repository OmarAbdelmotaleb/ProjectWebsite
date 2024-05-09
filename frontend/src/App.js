import React, { useState, useEffect } from 'react';
import './App.css'; // Assuming you'll add styles

function App() {
  const [count, setCount] = useState(0);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [loginError, setLoginError] = useState(false);

  useEffect(() => {
    // Fetch initial count (if a user is logged in)
    const fetchData = async () => {
      if (isLoggedIn) { // Only fetch if logged in 
        if (isLoggedIn) { 
          try {
            const response = await fetch('http://localhost:8000/api/users/me/'); // Assuming an endpoint to get the current user
            if (response.ok) {
              const data = await response.json();
              setCount(data.clicks);
            } else {
              console.error('Error fetching click count:', response.statusText);
            }
          } catch (error) {
            console.error('Error fetching click count:', error);
          }
        } 
      } 
    };
    fetchData(); 
  }, [isLoggedIn]); // Dependency on isLoggedIn

  const handleClick = async () => { 
    try {
      const response = await fetch(`http://localhost:8000/api/update-clicks/`, { // Update clicks for the logged-in user 
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        }
        // body: JSON.stringify({ clicks: count + 1 }) 
      });

      if (response.ok) {
        const data = await response.json(); 
        setCount(data.clicks); // Update the count 
      } else {
        console.error('Error updating click count:', response.statusText);
      }
    } catch (error) {
      console.error('Error updating click count:', error);
    }
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    // ... (add your fetch logic for '/api/login/')
    try {
      const response = await fetch('http://localhost:8000/api/login/', {  
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        setIsLoggedIn(true); 
        setLoginError(false);
      } else {
        setLoginError(true);
      }
    } catch (error) {
      console.error('Error logging in:', error);
    }
  };

  return (
    <div className="container"> 
      <div className="left-section">
        <h1>Click Count: {count}</h1>
        <button onClick={handleClick} disabled={!isLoggedIn}>Click Me!</button> 
      </div>

      <div className="right-section">
        <h2>Login</h2>
        <form onSubmit={handleLogin}>
          <input 
            type="text" 
            placeholder="Username" 
            value={username} 
            onChange={(e) => setUsername(e.target.value)} 
          /> 
          <input 
            type="password" 
            placeholder="Password" 
            value={password} 
            onChange={(e) => setPassword(e.target.value)} 
          /> 
          <button type="submit">Login</button>
        </form>
        {loginError && <p className="error-message">Incorrect login details</p>} 
      </div>
    </div>
  );
}

export default App;

// import React, { useState } from 'react';

// function App() {
//   const [count, setCount] = useState(0); 

//   const handleClick = () => {
//     setCount(count + 1); 
//   };

//   return (
//     <div>
//       <h1>Button Clicks: {count}</h1>
//       <button onClick={handleClick}>Click Me!</button>
//     </div>
//   );
// }

// export default App; 
