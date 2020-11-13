import axios from "axios"

const _api_root = "http://localhost:8000"

function get(path) {
  // returns Promise
  return axios.get(_api_root + path);
}


export default { get };
