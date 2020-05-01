const TwitchModule = require('twitch').default;
const F = require('fs');

const clientId = '85kp86tojs4oloqsdkq705x99bkdmd';
const clientSecret = '066i3rsrw2ku1l8y0q5qdxvfs633ak';
const TwitchClient = TwitchModule.withClientCredentials(clientId, clientSecret);

const TestUser = process.argv.slice(2).join();
get_user(TestUser).then(UltraHuso => F.writeFile("letzter_huso", UltraHuso._data.profile_image_url, function(){}))

async function get_user(Huso) {
    const user = await TwitchClient.helix.users.getUserByName(Huso);
    if (!user) {
        return false;
    }
    return await user;
}
