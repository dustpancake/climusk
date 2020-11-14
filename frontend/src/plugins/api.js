import axios from "axios"

const _api_root = "http://localhost:8000"

function get(path) {
  // returns Promise
  if (path == undefined) {
    path = "";
  }
  console.log(path);
  return axios.get(_api_root + path);
}

function healthcheck() {
  return axios.get(_api_root);
}

export default { get, healthcheck };
