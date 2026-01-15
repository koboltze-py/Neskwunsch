import React, { useState, useEffect } from 'react';
import ShiftRequestForm from './components/ShiftRequestForm';
import Login from './components/Login';
import * as api from './services/api';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isAdmin, setIsAdmin] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Prüfe ob Benutzer bereits eingeloggt ist
    checkAuthStatus();
  }, []);

  const checkAuthStatus = async () => {
    try {
      // Versuche, die Dienstwünsche zu laden - wenn erfolgreich, ist User eingeloggt
      const result = await api.getUserShiftRequests();
      if (result.success) {
        setIsAuthenticated(true);
      }
    } catch (error) {
      // Nicht eingeloggt
      setIsAuthenticated(false);
    } finally {
      setIsLoading(false);
    }
  };

  const handleLoginSuccess = (adminStatus: boolean) => {
    setIsAuthenticated(true);
    setIsAdmin(adminStatus);
    
    // Wenn Admin, zur Admin-Seite weiterleiten
    if (adminStatus) {
      window.location.href = '/admin';
    }
  };

  const handleLogout = async () => {
    await api.logout();
    setIsAuthenticated(false);
    setIsAdmin(false);
  };

  if (isLoading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center">
        <div className="text-center">
          <svg 
            className="animate-spin h-12 w-12 text-indigo-600 mx-auto mb-4" 
            xmlns="http://www.w3.org/2000/svg" 
            fill="none" 
            viewBox="0 0 24 24"
          >
            <circle 
              className="opacity-25" 
              cx="12" 
              cy="12" 
              r="10" 
              stroke="currentColor" 
              strokeWidth="4"
            />
            <path 
              className="opacity-75" 
              fill="currentColor" 
              d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
            />
          </svg>
          <p className="text-gray-600">Lädt...</p>
        </div>
      </div>
    );
  }

  if (!isAuthenticated) {
    return <Login onLoginSuccess={handleLoginSuccess} />;
  }

  return (
    <div className="App">
      {/* Logout Button oben rechts */}
      <div className="fixed top-4 right-4 z-50">
        <button
          onClick={handleLogout}
          className="bg-white hover:bg-gray-50 text-gray-700 font-medium py-2 px-4 rounded-lg shadow-md hover:shadow-lg transition-all duration-200 flex items-center"
        >
          <svg 
            className="w-5 h-5 mr-2" 
            fill="none" 
            stroke="currentColor" 
            viewBox="0 0 24 24"
          >
            <path 
              strokeLinecap="round" 
              strokeLinejoin="round" 
              strokeWidth={2} 
              d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" 
            />
          </svg>
          Abmelden
        </button>
      </div>
      
      <ShiftRequestForm />
    </div>
  );
}

export default App;
