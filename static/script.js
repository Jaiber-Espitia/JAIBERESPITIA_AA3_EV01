const getData = async(data) => {
    return await new Promise((resolve, reject) => {
        if (data) {
            resolve("resolved!")
        } else {
            reject(new Error("Error"))
        }
    })
}