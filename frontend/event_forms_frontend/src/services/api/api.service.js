import axios, { AxiosError } from "axios";

const apiURL = import.meta.env.VITE_BASE_API_URL

class ApiError extends Error {
    constructor(message, response) {
        super(message);
        this.response = response;
    }
}

export class ApiService {

    constructor(baseURL = apiURL) {
        this.baseURL = baseURL;
    }

    _getError(e) {
        if (e instanceof AxiosError) {
            /* Возвращаем ошибку, содержащую сообщение об ошибке и ответ сервера */
            /* Если имеем дело с ошибкой Axios, пытаемся получить сообщение, которое отправил бэкенд */
            return new ApiError(
                e.response.data?.error?.message ?? e.message,
                e.response
            );
        } else {
            /* Возвращаем ошибку, содержащую сообщение об ошибке и ответ сервера */
            return new ApiError(e.message, e.response);
        }
    }

    /* Функция для запросов без тела: GET, DELETE */
    _wrapper1(method, url) {
        return async () => {
            try {
                const response = await method(url);
                return {
                    __state: "success",
                    ...response,
                };
            } catch (e) {
                return {
                    __state: "error",
                    data: this._getError(e),
                };
            }
        };
    }

    /* Функция для запросов с телом: POST, PUT */
    _wrapper2(method, url, payload) {
        return async () => {
            try {
                const response = await method(url, payload);
                return {
                    __state: "success",
                    ...response,
                };
            } catch (e) {
                return {
                    __state: "error",
                    data: this._getError(e),
                };
            }
        };
    }

    $get(url) {
        return this._wrapper1(axios.get, `${this.baseURL}${url}`)();
    }

    $post(url, payload) {
        return this._wrapper2(axios.post, `${this.baseURL}${url}`, payload)();
    }

    $put(url, payload) {
        return this._wrapper2(axios.put, `${this.baseURL}${url}`, payload)();
    }

    $delete(url) {
        return this._wrapper1(axios.delete, `${this.baseURL}${url}`)();
    }
}