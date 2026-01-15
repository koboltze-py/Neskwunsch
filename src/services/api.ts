/**
 * API Service für Flask Backend
 * Zentrale Stelle für alle API-Aufrufe
 */

const API_BASE_URL = (import.meta as any).env?.VITE_API_URL || 'http://localhost:5000';

interface ApiResponse<T = any> {
  success: boolean;
  data?: T;
  error?: string;
}

interface ShiftRequestData {
  date: Date;
  shiftType: string;
  remarks?: string | null;
}

interface ShiftRequestResponse {
  id: string;
  user_name: string;
  date: string;
  shiftType: string;
  remarks: string;
  status: string;
  createdAt: string;
}

interface LoginData {
  name: string;
  password: string;
}

interface LoginResponse {
  is_admin: boolean;
}

/**
 * Helper-Funktion für API-Aufrufe mit Fehlerbehandlung
 */
async function apiCall<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<ApiResponse<T>> {
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      ...options,
      credentials: 'include', // Wichtig für Session-Cookies
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
    });

    const data = await response.json();

    if (!response.ok) {
      return {
        success: false,
        error: data.error || `HTTP ${response.status}: ${response.statusText}`,
      };
    }

    return data;
  } catch (error) {
    console.error('API Call Error:', error);
    return {
      success: false,
      error: error instanceof Error ? error.message : 'Netzwerkfehler',
    };
  }
}

// ==================== Auth API ====================

/**
 * Login oder Registrierung
 */
export async function login(credentials: LoginData): Promise<ApiResponse<LoginResponse>> {
  return apiCall<LoginResponse>('/login', {
    method: 'POST',
    body: JSON.stringify(credentials),
  });
}

/**
 * Logout
 */
export async function logout(): Promise<void> {
  await fetch(`${API_BASE_URL}/logout`, {
    credentials: 'include',
  });
}

// ==================== Shift Request API ====================

/**
 * Erstelle einen neuen Dienstwunsch
 */
export async function createShiftRequest(
  data: ShiftRequestData
): Promise<ApiResponse<ShiftRequestResponse>> {
  // Konvertiere Date zu ISO String
  const requestData = {
    date: data.date.toISOString(),
    shiftType: data.shiftType,
    remarks: data.remarks || '',
  };

  return apiCall<ShiftRequestResponse>('/api/shift-requests', {
    method: 'POST',
    body: JSON.stringify(requestData),
  });
}

/**
 * Hole alle Dienstwünsche des aktuellen Benutzers (aktueller Monat)
 */
export async function getUserShiftRequests(): Promise<ApiResponse<ShiftRequestResponse[]>> {
  return apiCall<ShiftRequestResponse[]>('/api/shift-requests', {
    method: 'GET',
  });
}

/**
 * Lösche einen Dienstwunsch
 */
export async function deleteShiftRequest(requestId: string): Promise<ApiResponse<void>> {
  return apiCall<void>(`/api/shift-requests/${requestId}`, {
    method: 'DELETE',
  });
}

export default {
  login,
  logout,
  createShiftRequest,
  getUserShiftRequests,
  deleteShiftRequest,
};
