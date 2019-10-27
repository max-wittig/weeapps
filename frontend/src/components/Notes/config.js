export const EXPIRES = Object.freeze({
    "THIRTY_MINUTES": 1, 
    "ONE_HOUR": 2,
    "FIVE_HOURS": 3,
    "FIFTEEN_HOURS": 4,
    "ONE_DAY": 5,
    "ONE_WEEK": 6,
});
export const EXPIRES_IN_SECONDS = Object.freeze({
    0: 0,
    1: 60 * 30, 
    2: 60 * 60,
    3: 60 * 60 * 5,
    4: 60 * 60 * 15,
    5: 60 * 60 * 24,
    6: 60 * 60 * 24 * 7,
});
