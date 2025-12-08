/**
 * Constrói a configuração de AppConfig a partir do workspace Blockly.
 * Assume:
 *  - Exatamente um bloco AppConfig no topo.
 *  - Blocos filhos para Accounts, Listings, Messaging, Ratings, Payments,
 *    Logistics, Subcommunities, AccessPolicies conectados nas inputs correspondentes.
 */
function buildConfigFromWorkspace(workspace) {
  var topBlocks = workspace.getTopBlocks(false);
  var appBlocks = topBlocks.filter(b => b.type === "AppConfig");

  if (appBlocks.length !== 1) {
    return null;
  }

  var app = appBlocks[0];

  var config = {
    appName: app.getFieldValue("APPNAME") || "",
    shortName: app.getFieldValue("SHORTNAME") || "",
    logoUrl: app.getFieldValue("LOGOURL") || "",
    primaryColor: app.getFieldValue("PRIMARYCOLOR") || "",
    secondaryColor: app.getFieldValue("SECONDARYCOLOR") || "",
    accounts: null,
    listings: null,
    messaging: null,
    ratings: null,
    payments: null,
    logistics: null,
    subcommunities: null,
    accessPolicies: null
  };

  // Inputs que ligam para outros blocos

  console.log(app)

  config.accounts = buildAccounts(app.getInputTargetBlock("ACCOUNTS"));
  config.listings = buildListings(app.getInputTargetBlock("LISTINGS"));
  config.messaging = buildMessaging(app.getInputTargetBlock("MESSAGING"));
  config.ratings = buildRatings(app.getInputTargetBlock("RATINGS"));
  config.payments = buildPayments(app.getInputTargetBlock("PAYMENTS"));
  config.logistics = buildLogistics(app.getInputTargetBlock("LOGISTICS"));
  config.subcommunities = buildSubcommunities(app.getInputTargetBlock("SUBCOMMUNITIES"));
  config.accessPolicies = buildAccessPolicies(app.getInputTargetBlock("ACCESSPOLICIES"));

  console.log(app.getInputTargetBlock("ACCOUNTS"))

  console.log(buildAccounts(app.getInputTargetBlock("ACCOUNTS")))

  return config;
}

/* Helpers para cada tipo de bloco */

function buildAccounts(block) {
  if (!block || block.type !== "Accounts") return null;
  return {
    localLogin: block.getFieldValue("LOCALLOGIN") === "TRUE",
    oauthLogin: block.getFieldValue("OAUTHLOGIN") === "TRUE",
    phoneVerification: block.getFieldValue("PHONEVERIFICATION") === "TRUE",
    moderators: block.getFieldValue("MODERATORS") === "TRUE"
  };
}

function buildListings(block) {
  if (!block || block.type !== "Listings") return null;
  return {
    products: block.getFieldValue("PRODUCTS") === "TRUE",
    services: block.getFieldValue("SERVICES") === "TRUE",
    priceMode: block.getFieldValue("PRICEMODE") === "TRUE",
    exchangeMode: block.getFieldValue("EXCHANGEMODE") === "TRUE",
    donationMode: block.getFieldValue("DONATIONMODE") === "TRUE",
    expiry: block.getFieldValue("EXPIRY") === "TRUE",
    variants: block.getFieldValue("VARIANTS") === "TRUE",
    currency: block.getFieldValue("CURRENCY") || "EUR",
    minPrice: Number(block.getFieldValue("MINPRICE") || 0),
    maxPrice: Number(block.getFieldValue("MAXPRICE") || 0)
  };
}

function buildMessaging(block) {
  if (!block || block.type !== "Messaging") return null;
  return {
    chat: block.getFieldValue("CHAT") === "TRUE",
    imagesInChat: block.getFieldValue("IMAGESINCHAT") === "TRUE"
  };
}

function buildRatings(block) {
  if (!block || block.type !== "Ratings") return null;
  return {
    simple: block.getFieldValue("SIMPLE") === "TRUE",
    bidirectional: block.getFieldValue("BIDIRECTIONAL") === "TRUE"
  };
}

function buildPayments(block) {
  if (!block || block.type !== "Payments") return null;
  return {
    mbway: block.getFieldValue("MBWAY") === "TRUE",
    multibanco: block.getFieldValue("MULTIBANCO") === "TRUE",
    paypal: block.getFieldValue("PAYPAL") === "TRUE",
    none: block.getFieldValue("NONE") === "TRUE",
    publicKey: block.getFieldValue("PUBLICKEY") || "",
    secretRef: block.getFieldValue("SECRETREF") || ""
  };
}

function buildLogistics(block) {
  if (!block || block.type !== "Logistics") return null;
  return {
    inPerson: block.getFieldValue("INPERSON") === "TRUE",
    mail: block.getFieldValue("MAIL") === "TRUE",
    locker: block.getFieldValue("LOCKER") === "TRUE"
  };
}

function buildSubcommunities(block) {
  if (!block || block.type !== "Subcommunities") return null;
  return {
    enabled: block.getFieldValue("ENABLED") === "TRUE"
  };
}

function buildAccessPolicies(block) {
  if (!block || block.type !== "AccessPolicies") return null;
  return {
    anonymousBrowse: block.getFieldValue("ANONYMOUSBROWSE") === "TRUE",
    anonymousMessages: block.getFieldValue("ANONYMOUSMESSAGES") === "TRUE"
  };
}
