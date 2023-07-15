CREATE TABLE CoinMarket (
    id SERIAL PRIMARY KEY,
    CoinName VARCHAR,
    CoinPrice FLOAT,
    CoinAmount FLOAT,
    CoinATH FLOAT,
    CoinValue FLOAT,
    CoinValueATH FLOAT
);
