Blockly.defineBlocksWithJsonArray(
[
  /* AppConfig (root) */
  {
    "type": "AppConfig",
    "message0": "AppConfig appName %1 shortName %2 logoUrl %3 primaryColor %4 secondaryColor %5 accounts %6 listings %7 messaging %8 ratings %9 payments %10 logistics %11 subcommunities %12 accessPolicies %13",
    "args0": [
      {
        "type": "field_input",
        "name": "APPNAME",
        "text": "appName"
      },
      {
        "type": "field_input",
        "name": "SHORTNAME",
        "text": "shortName"
      },
      {
        "type": "field_input",
        "name": "LOGOURL",
        "text": "logoUrl"
      },
      {
        "type": "field_input",
        "name": "PRIMARYCOLOR",
        "text": "#123456"
      },
      {
        "type": "field_input",
        "name": "SECONDARYCOLOR",
        "text": "#654321"
      },
      {
        "type": "input_value",
        "name": "ACCOUNTS",
        "check": "Accounts"
      },
      {
        "type": "input_value",
        "name": "LISTINGS",
        "check": "Listings"
      },
      {
        "type": "input_value",
        "name": "MESSAGING",
        "check": "Messaging"
      },
      {
        "type": "input_value",
        "name": "RATINGS",
        "check": "Ratings"
      },
      {
        "type": "input_value",
        "name": "PAYMENTS",
        "check": "Payments"
      },
      {
        "type": "input_value",
        "name": "LOGISTICS",
        "check": "Logistics"
      },
      {
        "type": "input_value",
        "name": "SUBCOMMUNITIES",
        "check": "Subcommunities"
      },
      {
        "type": "input_value",
        "name": "ACCESSPOLICIES",
        "check": "AccessPolicies"
      }
    ],
    "colour": 210,
    "tooltip": "Root AppConfig for the community DSML",
    "helpUrl": ""
  },

  /* Accounts */
  {
    "type": "Accounts",
    "message0": "Accounts localLogin %1 oauthLogin %2 phoneVerification %3 moderators %4",
    "args0": [
      {
        "type": "field_checkbox",
        "name": "LOCALLOGIN"
      },
      {
        "type": "field_checkbox",
        "name": "OAUTHLOGIN"
      },
      {
        "type": "field_checkbox",
        "name": "PHONEVERIFICATION"
      },
      {
        "type": "field_checkbox",
        "name": "MODERATORS"
      }
    ],
    "colour": 230,
    "output": "Accounts",
    "tooltip": "Accounts configuration (logins, verification, moderators)",
    "helpUrl": ""
  },

  /* Listings */
  {
    "type": "Listings",
    "message0": "Listings products %1 services %2 priceMode %3 exchangeMode %4 donationMode %5 expiry %6 variants %7 currency %8 minPrice %9 maxPrice %10",
    "args0": [
      {
        "type": "field_checkbox",
        "name": "PRODUCTS"
      },
      {
        "type": "field_checkbox",
        "name": "SERVICES"
      },
      {
        "type": "field_checkbox",
        "name": "PRICEMODE"
      },
      {
        "type": "field_checkbox",
        "name": "EXCHANGEMODE"
      },
      {
        "type": "field_checkbox",
        "name": "DONATIONMODE"
      },
      {
        "type": "field_checkbox",
        "name": "EXPIRY"
      },
      {
        "type": "field_checkbox",
        "name": "VARIANTS"
      },
      {
        "type": "field_input",
        "name": "CURRENCY",
        "text": "EUR"
      },
      {
        "type": "field_number",
        "name": "MINPRICE",
        "value": 0
      },
      {
        "type": "field_number",
        "name": "MAXPRICE",
        "value": 0
      }
    ],
    "colour": 250,
    "output": "Listings",
    "tooltip": "Listings configuration (types, pricing, currency, ranges)",
    "helpUrl": ""
  },

  /* Messaging */
  {
    "type": "Messaging",
    "message0": "Messaging chat %1 imagesInChat %2",
    "args0": [
      {
        "type": "field_checkbox",
        "name": "CHAT"
      },
      {
        "type": "field_checkbox",
        "name": "IMAGESINCHAT"
      }
    ],
    "colour": 270,
    "output": "Messaging",
    "tooltip": "Messaging configuration (chat and images in chat)",
    "helpUrl": ""
  },

  /* Ratings */
  {
    "type": "Ratings",
    "message0": "Ratings simple %1 bidirectional %2",
    "args0": [
      {
        "type": "field_checkbox",
        "name": "SIMPLE"
      },
      {
        "type": "field_checkbox",
        "name": "BIDIRECTIONAL"
      }
    ],
    "colour": 290,
    "output": "Ratings",
    "tooltip": "Ratings configuration (simple vs bidirectional)",
    "helpUrl": ""
  },

  /* Payments */
  {
    "type": "Payments",
    "message0": "Payments mbway %1 multibanco %2 paypal %3 none %4 publicKey %5 secretRef %6",
    "args0": [
      {
        "type": "field_checkbox",
        "name": "MBWAY"
      },
      {
        "type": "field_checkbox",
        "name": "MULTIBANCO"
      },
      {
        "type": "field_checkbox",
        "name": "PAYPAL"
      },
      {
        "type": "field_checkbox",
        "name": "NONE"
      },
      {
        "type": "field_input",
        "name": "PUBLICKEY",
        "text": "publicKey"
      },
      {
        "type": "field_input",
        "name": "SECRETREF",
        "text": "secretRef"
      }
    ],
    "colour": 310,
    "output": "Payments",
    "tooltip": "Payments configuration (methods and keys)",
    "helpUrl": ""
  },

  /* Logistics */
  {
    "type": "Logistics",
    "message0": "Logistics inPerson %1 mail %2 locker %3",
    "args0": [
      {
        "type": "field_checkbox",
        "name": "INPERSON"
      },
      {
        "type": "field_checkbox",
        "name": "MAIL"
      },
      {
        "type": "field_checkbox",
        "name": "LOCKER"
      }
    ],
    "colour": 330,
    "output": "Logistics",
    "tooltip": "Logistics configuration (in person, mail, locker)",
    "helpUrl": ""
  },

  /* Subcommunities */
  {
    "type": "Subcommunities",
    "message0": "Subcommunities enabled %1",
    "args0": [
      {
        "type": "field_checkbox",
        "name": "ENABLED"
      }
    ],
    "colour": 350,
    "output": "Subcommunities",
    "tooltip": "Subcommunities configuration (enabled/disabled)",
    "helpUrl": ""
  },

  /* AccessPolicies */
  {
    "type": "AccessPolicies",
    "message0": "AccessPolicies anonymousBrowse %1 anonymousMessages %2",
    "args0": [
      {
        "type": "field_checkbox",
        "name": "ANONYMOUSBROWSE"
      },
      {
        "type": "field_checkbox",
        "name": "ANONYMOUSMESSAGES"
      }
    ],
    "colour": 10,
    "output": "AccessPolicies",
    "tooltip": "Access policies configuration (anonymous access)",
    "helpUrl": ""
  }
]
);
