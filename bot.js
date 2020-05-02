require('dotenv').config();
const TwitchModule = require('twitch').default;
const clientId = process.env.clientId;
const clientSecret = process.env.clientSecret;
const F = require('fs');

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
