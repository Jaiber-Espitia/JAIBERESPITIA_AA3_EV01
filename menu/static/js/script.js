const removeUsernameAfterThreeSeconds = () => {
    setTimeout(() => {
        $("#username").hide()
    }, 3000)
};



removeUsernameAfterThreeSeconds();